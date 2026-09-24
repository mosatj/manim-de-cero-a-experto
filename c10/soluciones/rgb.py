from manim import *


class Rgb(Scene):
    def construct(self):
        colores = [PURE_RED, PURE_GREEN, PURE_BLUE]
        circulos = VGroup(*[
            Circle(1.6, stroke_width=0, fill_color=c,
                   fill_opacity=0.5)
            .move_to(1.1 * rotate_vector(UP, k * TAU / 3))
            for k, c in enumerate(colores)
        ])
        self.add(circulos)
