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


def dfs_eventos(ady, u, visitado=None, pila=None):
    """DFS recursivo; 'yield from' reenvía los eventos hijos."""
    visitado = set() if visitado is None else visitado
    pila = [] if pila is None else pila
    visitado.add(u)
    pila.append(u)
    yield "entra", u, None, list(pila)
    for v in ady[u]:
        if v not in visitado:
            yield "arista", v, u, list(pila)
            yield from dfs_eventos(ady, v, visitado, pila)
    pila.pop()
    yield "sale", u, None, list(pila)


def arista(g, u, v):
    return g.edges[(u, v)] if (u, v) in g.edges else g.edges[(v, u)]


class BusquedaProfundidad(Scene):
    def construct(self):
        aristas = [(u, v) for u in ADYACENCIA
                   for v in ADYACENCIA[u] if u < v]
        g = Graph(list(ADYACENCIA), aristas, layout=POSICIONES,
                  labels=True,
                  vertex_config={"radius": 0.3,
                                 "fill_color": GREY_B},
                  edge_config={"stroke_color": GREY_C})
        titulo = Tex("Recorrido en profundidad (DFS) desde A",
                     font_size=36).to_edge(UP, buff=0.2)
        self.add(g, titulo)

        def dibujar_pila(pila):
            celdas = [VGroup(Rectangle(width=0.9, height=0.5,
                                       color=ORANGE),
                             Tex(f"dfs({v})", font_size=24))
                      for v in pila]
            rotulo = Tex("pila de llamadas:", font_size=32)
            grupo = VGroup(rotulo, *celdas)
            grupo.arrange(RIGHT, buff=0.12)
            return grupo.to_edge(DOWN, buff=0.5)

        pila_dibujo = dibujar_pila([])
        self.add(pila_dibujo)
        orden = 0
        for tipo, v, padre, pila in dfs_eventos(ADYACENCIA, "A"):
            nueva = dibujar_pila(pila)
            anims = [FadeOut(pila_dibujo), FadeIn(nueva)]
            if tipo == "entra":               # primera visita
                orden += 1
                numero = MathTex(str(orden), font_size=30,
                                 color=ORANGE)
                color = g[v].animate.set_fill(ORANGE, family=False)
                anims += [color,
                          FadeIn(numero.next_to(g[v], UP, 0.1))]
            elif tipo == "arista":            # arista del árbol
                anims.append(arista(g, padre, v).animate
                             .set_stroke(ORANGE, width=7))
            else:                             # la llamada termina
                anims.append(g[v].animate.set_fill(BLUE_C,
                                                   family=False))
            self.play(*anims, run_time=0.6)
            pila_dibujo = nueva
        self.wait()
