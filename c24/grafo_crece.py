from manim import *


class GrafoCrece(Scene):
    def construct(self):
        estilo = {"radius": 0.25, "fill_color": TEAL_C}
        g = Graph(["A"], [], labels=True, vertex_config=estilo)
        self.play(Create(g))
        # .animate sobre add_vertices y add_edges crea la animación
        self.play(g.animate.add_vertices(
            "B", "C", labels=True, vertex_config=estilo,
            positions={"B": [-2, -1.5, 0], "C": [2, -1.5, 0]}))
        self.play(g.animate.add_edges(
            ("A", "B"), ("A", "C"), edge_config={"color": YELLOW}))
        # Una arista con un vértice nuevo lo crea; los demás
        # argumentos con nombre pasan a add_vertices
        self.play(g.animate.add_edges(
            ("B", "D"), ("C", "D"), positions={"D": [0, -3, 0]},
            labels=True, vertex_config=estilo))
        self.play(g.animate.remove_edges(("A", "C")))
        self.play(g.animate.remove_vertices("B"))
        self.wait()
