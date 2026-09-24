from manim import *


class CadenaCorrecta(Scene):
    def construct(self):
        a = Circle(radius=1, color=BLUE, fill_opacity=0.6)
        a.shift(4 * LEFT)
        b = Square(side_length=2, color=TEAL, fill_opacity=0.6)
        c = Triangle(color=YELLOW, fill_opacity=0.6).scale(1.4)
        c.shift(4 * RIGHT)

        self.play(Create(a))
        self.play(ReplacementTransform(a, b))  # b entra en escena
        self.play(ReplacementTransform(b, c))  # y c sustituye a b
