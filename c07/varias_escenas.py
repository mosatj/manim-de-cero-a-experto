from manim import *


class EscenaUno(Scene):
    def construct(self):
        self.play(Create(Circle(radius=2, color=BLUE)))


class EscenaDos(Scene):
    def construct(self):
        self.play(DrawBorderThenFill(
            Square(side_length=3, color=GREEN,
                   fill_opacity=0.5)))
