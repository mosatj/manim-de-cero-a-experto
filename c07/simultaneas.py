from manim import *


class Simultaneas(Scene):
    def construct(self):
        rect = RoundedRectangle(color=RED)
        tri = Triangle(color=BLUE)
        tri.set_fill(BLUE, 0.5).scale(2)
        rect.shift(LEFT * 3)
        tri.shift(RIGHT * 3)
        self.play(Create(rect),
                  DrawBorderThenFill(tri))
