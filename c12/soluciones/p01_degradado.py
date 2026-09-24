from manim import *


class Degradado(Scene):
    def construct(self):
        circulos = VGroup(*[Circle(radius=0.6, fill_opacity=0.7)
                            for _ in range(7)])
        circulos.arrange(RIGHT, buff=0.2)
        n = len(circulos)
        for k, c in enumerate(circulos):
            c.set_color(interpolate_color(BLUE, RED, k / (n - 1)))
        self.add(circulos)
