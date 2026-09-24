from manim import *


class Transformar(Scene):
    def construct(self):
        rect = RoundedRectangle(color=RED)
        tri = Triangle(color=BLUE).scale(2)
        self.add(rect)
        self.wait()
        self.play(Transform(rect, tri))
        self.play(rect.animate.scale(0.5))
