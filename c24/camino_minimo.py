import networkx as nx
from manim import *

PESOS = {("A", "B"): 4, ("A", "C"): 2, ("B", "C"): 1,
         ("B", "D"): 5, ("C", "D"): 8, ("C", "E"): 10,
         ("D", "E"): 2, ("D", "F"): 6, ("E", "F"): 2}
POSICIONES = {"A": [-5.5, 0, 0], "B": [-3, 2, 0], "C": [-3, -2, 0],
              "D": [0, 2, 0], "E": [0, -2, 0], "F": [2.5, 0, 0]}


class CaminoMinimo(Scene):
    def construct(self):
        # networkx calcula; Manim solo muestra
        G = nx.Graph()
        for (u, v), w in PESOS.items():
            G.add_edge(u, v, peso=w)
        camino = nx.dijkstra_path(G, "A", "F", weight="peso")
        costo = nx.dijkstra_path_length(G, "A", "F", weight="peso")

        g = Graph.from_networkx(
            G, layout=POSICIONES, labels=True,
            vertex_config={"radius": 0.32},
            edge_config={"stroke_color": GREY_C})
        pesos = VGroup(*[
            MathTex(str(w), font_size=30).move_to(g.edges[e])
            .add_background_rectangle() for e, w in PESOS.items()])
        self.add(g, pesos)
        for u, v in zip(camino, camino[1:]):
            e = (u, v) if (u, v) in g.edges else (v, u)
            self.play(g[u].animate.set_fill(RED_C, family=False),
                      g.edges[e].animate.set_stroke(RED_C, width=8),
                      run_time=0.6)
        ultimo = g[camino[-1]]
        self.play(ultimo.animate.set_fill(RED_C, family=False))
        texto = (r" \to ".join(camino)
                 + rf"\quad(\text{{costo}} = {costo})")
        resumen = MathTex(texto, font_size=40, color=RED_C)
        self.play(Write(resumen.to_edge(DOWN)))
        self.wait()
