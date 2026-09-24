from manim import *


class Ecuacion(Scene):
    def construct(self):
        pasos = MathTex(
            r"3x - 5 &= 10 \\",
            r"3x &= 15 \\",
            r"x &= \frac{15}{3} \\",
            r"x &= 5",
            font_size=64,
        )
        for paso in pasos:
            self.play(Write(paso))
        self.play(Create(SurroundingRectangle(pasos[-1])))
