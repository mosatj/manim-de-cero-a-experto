from manim import *


class CicloDirigido(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5]
        # 1→2→…→5→1
        aristas = [(k, k % 5 + 1) for k in vertices]
        g = DiGraph(vertices, aristas, labels=True,
                    layout={k: [2 * k - 6, 0, 0] for k in vertices},
                    edge_config={"stroke_width": 3})
        self.play(Create(g))
        self.play(g.animate.change_layout("circular",
                                          layout_scale=2.5))
        self.wait()
