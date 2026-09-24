from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


def fichas(n):
    """n cuadrados numerados, en un VGroup."""
    return VGroup(*[
        VGroup(Square(1.0, color=BLUE, fill_opacity=0.35),
               Text(str(k), font_size=36))
        for k in range(1, n + 1)
    ])


class Cuadricula(Scene):
    def construct(self):
        a = fichas(12).arrange_in_grid(rows=3, cols=4, buff=0.15)
        b = fichas(12).arrange_in_grid(rows=3, cols=4, buff=0.15,
                                       flow_order="dr")
        VGroup(a, b).arrange(RIGHT, buff=1.2).shift(0.4 * UP)
        self.add(a, b)
        self.add(Text('flow_order="rd" (defecto)', font_size=26)
                 .next_to(a, DOWN))
        self.add(Text('flow_order="dr"', font_size=26)
                 .next_to(b, DOWN))
        titulo = "arrange_in_grid(rows=3, cols=4, buff=0.15)"
        self.add(Text(titulo, font_size=30, color=YELLOW)
                 .to_edge(UP))
