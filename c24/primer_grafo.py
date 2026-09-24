from manim import *


class PrimerGrafo(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5]
        aristas = [(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (2, 5)]
        posiciones = {1: [-3, 1, 0], 2: [0, 2, 0], 3: [-1, -1.5, 0],
                      4: [2, -1.5, 0], 5: [3, 1, 0]}
        g = Graph(vertices, aristas, layout=posiciones, labels=True,
                  vertex_config={"radius": 0.3,
                                 "fill_color": BLUE_B},
                  edge_config={"stroke_width": 5})
        self.play(Create(g), run_time=2)
        # Vértices y aristas se piden como en un diccionario
        self.play(Indicate(g[3]))
        self.play(g[3].animate.set_fill(YELLOW, family=False))
        self.play(g.edges[(3, 4)].animate.set_color(RED_C))
        # Mover un vértice arrastra sus aristas (actualizador)
        self.play(g[5].animate.move_to([3, -0.5, 0]))
        self.wait()
