import heapq
from manim import *

PESOS = {("A", "B"): 4, ("A", "C"): 2, ("B", "C"): 1,
         ("B", "D"): 5, ("C", "D"): 8, ("C", "E"): 10,
         ("D", "E"): 2, ("D", "F"): 6, ("E", "F"): 2}
POSICIONES = {"A": [-5.5, 0, 0], "B": [-3, 2, 0], "C": [-3, -2, 0],
              "D": [0, 2, 0], "E": [0, -2, 0], "F": [2.5, 0, 0]}


def dijkstra_eventos(pesos, origen):
    ady = {}
    for (u, v), w in pesos.items():        # grafo no dirigido
        ady.setdefault(u, []).append((v, w))
        ady.setdefault(v, []).append((u, w))
    dist = {v: float("inf") for v in ady}
    dist[origen], previo, fijos = 0, {}, set()
    monticulo = [(0, origen)]              # cola de prioridad
    while monticulo:
        d, u = heapq.heappop(monticulo)    # el más cercano
        if u in fijos:
            continue                       # entrada vieja
        fijos.add(u)
        yield "fija", u, None, d, sorted(monticulo)
        for v, w in ady[u]:
            if v not in fijos and d + w < dist[v]:  # relajación
                antes = previo.get(v)
                dist[v], previo[v] = d + w, u
                heapq.heappush(monticulo, (dist[v], v))
                yield ("mejora", v, (u, antes), dist[v],
                       sorted(monticulo))


class Dijkstra(Scene):
    def construct(self):
        g = Graph(list(POSICIONES), list(PESOS), layout=POSICIONES,
                  labels=True,
                  vertex_config={"radius": 0.32,
                                 "fill_color": GREY_B},
                  edge_config={"stroke_color": GREY_C,
                               "stroke_width": 4})
        pesos = VGroup(*[
            MathTex(str(w), font_size=30, color=GREY_A)
            .move_to(g.edges[e]).add_background_rectangle()
            for e, w in PESOS.items()])
        etiquetas = {}
        for v in POSICIONES:
            texto = "0" if v == "A" else r"\infty"
            lado = UP if g[v].get_y() >= 0 else DOWN
            rotulo = MathTex(texto, font_size=34, color=YELLOW)
            etiquetas[v] = rotulo.next_to(g[v], lado)
        self.add(g, pesos, *etiquetas.values())

        def dibujar_cola(cola):
            filas = [MathTex(rf"{v}:\,{d}", font_size=32)
                     for d, v in cola]
            if not filas:
                filas = [Tex("vacía", font_size=30)]
            grupo = VGroup(Tex("cola", font_size=34), *filas)
            grupo.arrange(DOWN, buff=0.18)
            return grupo.to_edge(RIGHT, buff=0.6)

        def arista(u, v):
            e = (u, v) if (u, v) in g.edges else (v, u)
            return g.edges[e]

        cola = dibujar_cola([(0, "A")])
        self.add(cola)
        eventos = dijkstra_eventos(PESOS, "A")
        for tipo, v, info, d, monticulo in eventos:
            nueva = dibujar_cola(monticulo)
            anims = [FadeOut(cola), FadeIn(nueva)]
            if tipo == "fija":               # distancia definitiva
                anims.append(g[v].animate.set_fill(BLUE_C,
                                                   family=False))
            else:
                u, antes = info
                texto = MathTex(str(d), font_size=34, color=YELLOW)
                texto.move_to(etiquetas[v])
                nueva_arista = arista(u, v).animate.set_stroke(
                    YELLOW, 7)
                anims += [Transform(etiquetas[v], texto),
                          nueva_arista]
                if antes is not None:        # el camino viejo sale
                    anims.append(arista(antes, v).animate
                                 .set_stroke(GREY_C, 4))
            self.play(*anims, run_time=0.8)
            cola = nueva
        self.wait()
