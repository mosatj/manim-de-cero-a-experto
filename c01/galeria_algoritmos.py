from manim import *


class GaleriaAlgoritmos(Scene):
    def construct(self):
        vertices = list(range(1, 11))
        aristas = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7),
                   (4, 8), (5, 9), (7, 10)]
        grafo = Graph(vertices, aristas, layout="tree", root_vertex=1,
                      labels=True, layout_scale=3.2,
                      vertex_config={"radius": 0.3})
        # Colorear los vértices por nivel, como en un recorrido en anchura
        niveles = [[1], [2, 3], [4, 5, 6, 7], [8, 9, 10]]
        colores = [RED, ORANGE, YELLOW, GREEN]
        for nivel, color in zip(niveles, colores):
            for v in nivel:
                grafo[v].set_fill(color, family=False)
        self.add(grafo)
