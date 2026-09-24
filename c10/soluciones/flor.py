from manim import *


class Flor(Scene):
    def construct(self):
        n = 10
        petalo = Ellipse(width=0.9, height=2.6, fill_opacity=0.7)
        petalo.shift(1.4 * UP)
        petalos = VGroup(*[
            petalo.copy().rotate(k * TAU / n, about_point=ORIGIN)
            for k in range(n)
        ])
        petalos.set_color_by_gradient(PINK, PURPLE, BLUE)
        centro = Circle(0.6, color=YELLOW, fill_opacity=1)
        self.add(petalos, centro)
