from itertools import combinations
from manim import *


class GrafoCompleto(Scene):
    def construct(self):
        vertices = list(range(1, 7))
        # 15 aristas
        aristas = list(combinations(vertices, 2))
        colores = color_gradient([BLUE_C, PURPLE_C, RED_C],
                                 len(aristas))
        g = Graph(vertices, aristas, layout="circular",
                  layout_scale=3,
                  labels=True, vertex_config={"radius": 0.3},
                  edge_config={e: {"stroke_color": c,
                                   "stroke_width": 4}
                               for e, c in zip(aristas, colores)})
        rotulo = MathTex(r"K_6:\ \binom{6}{2} = 15\text{ aristas}")
        g.shift(1.5 * RIGHT)
        self.play(Create(g), run_time=3)
        self.play(Write(rotulo.to_corner(UL)))
        self.wait()
