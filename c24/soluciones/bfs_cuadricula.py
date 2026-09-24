import networkx as nx
from manim import *


class BfsCuadricula(Scene):
    def construct(self):
        # vértices (i, j)
        G = nx.grid_2d_graph(6, 6)
        distancia = nx.single_source_shortest_path_length(G, (0, 0))
        maximo = max(distancia.values())
        g = Graph(list(G.nodes), list(G.edges),
                  layout={(i, j): [i - 2.5, j - 2.5, 0]
                          for i, j in G},
                  vertex_config={"radius": 0.2},
                  edge_config={"stroke_color": GREY_D})
        self.add(g)
        # Una «ola» por nivel: los vértices a distancia d a la vez
        for d in range(maximo + 1):
            color = interpolate_color(YELLOW, PURPLE_D, d / maximo)
            self.play(*[g[v].animate.set_fill(color)
                        for v, dv in distancia.items() if dv == d],
                      run_time=0.4)
        self.wait()
