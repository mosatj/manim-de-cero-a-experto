from manim import *


class Ventanas(Scene):
    def construct(self):
        cuadrados = VGroup(*[
            Square(side_length=1.5, color=c, fill_opacity=0.7)
            for c in (BLUE, TEAL, YELLOW)
        ]).arrange(RIGHT, buff=1).shift(2 * LEFT + DOWN)
        ventanas = [(0.0, 0.4), (0.3, 0.7), (0.6, 1.0)]
        self.add(cuadrados)
        # Un solo play: cada animación se mueve en su ventana
        self.play(*[
            c.animate(rate_func=squish_rate_func(smooth, a, b))
            .shift(3 * UP + 2 * RIGHT)
            for c, (a, b) in zip(cuadrados, ventanas)
        ], run_time=3)
