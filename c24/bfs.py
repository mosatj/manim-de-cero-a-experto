from collections import deque
from manim import *

ADYACENCIA = {
    "A": ["B", "C"], "B": ["A", "D", "E"], "C": ["A", "E"],
    "D": ["B", "F"], "E": ["B", "C", "F", "G"],
    "F": ["D", "E", "H"], "G": ["E", "H"], "H": ["F", "G"],
}
POSICIONES = {"A": [-5, 0.8, 0], "B": [-3, 2.4, 0],
              "C": [-3, -0.8, 0], "D": [-0.5, 2.4, 0],
              "E": [-0.5, -0.8, 0], "F": [2, 0.8, 0],
              "G": [2, -1.9, 0], "H": [4.5, 0.8, 0]}


def bfs_eventos(adyacencia, inicio):
    """BFS que no dibuja nada: solo anuncia lo que ocurre."""
    distancia = {inicio: 0}
    cola = deque([inicio])
    yield "descubre", inicio, None, 0, list(cola)
    while cola:
        u = cola.popleft()
        yield "saca", u, None, distancia[u], list(cola)
        for v in adyacencia[u]:
            if v not in distancia:
                distancia[v] = distancia[u] + 1
                cola.append(v)
                yield "descubre", v, u, distancia[v], list(cola)


def arista(g, u, v):
    """Un Graph guarda la arista como se escribió: (u,v) o (v,u)."""
    return g.edges[(u, v)] if (u, v) in g.edges else g.edges[(v, u)]


class BusquedaAnchura(Scene):
    def construct(self):
        aristas = [(u, v) for u in ADYACENCIA
                   for v in ADYACENCIA[u] if u < v]
        g = Graph(list(ADYACENCIA), aristas, layout=POSICIONES,
                  labels=True,
                  vertex_config={"radius": 0.3,
                                 "fill_color": GREY_B},
                  edge_config={"stroke_color": GREY_C})
        titulo = Tex("Recorrido en anchura (BFS) desde A",
                     font_size=36).to_edge(UP, buff=0.2)
        self.add(g, titulo)

        def dibujar_cola(cola):
            celdas = [VGroup(Square(0.6, color=YELLOW),
                             MathTex(v, font_size=34))
                      for v in cola]
            grupo = VGroup(Tex("cola:", font_size=34), *celdas)
            grupo.arrange(RIGHT, buff=0.15)
            return grupo.to_edge(DOWN, buff=0.5)

        cola_dibujo = dibujar_cola([])
        self.add(cola_dibujo)
        for tipo, v, padre, d, cola in bfs_eventos(ADYACENCIA, "A"):
            nueva = dibujar_cola(cola)
            anims = [FadeOut(cola_dibujo), FadeIn(nueva)]
            # family=False: se rellena el disco, no su letra
            if tipo == "descubre":            # entra en la cola
                anims.append(g[v].animate.set_fill(YELLOW,
                                                   family=False))
                marca = MathTex(f"d={d}", font_size=28,
                                color=YELLOW)
                anims.append(FadeIn(marca.next_to(g[v], UP, 0.1)))
                if padre is not None:         # arista del árbol
                    anims.append(arista(g, padre, v).animate
                                 .set_stroke(YELLOW, width=7))
            else:                             # sale de la cola
                anims.append(g[v].animate.set_fill(BLUE_C,
                                                   family=False))
            self.play(*anims, run_time=0.7)
            cola_dibujo = nueva
        self.wait()
