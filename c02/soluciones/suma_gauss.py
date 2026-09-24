from manim import *


class SumaGauss(Scene):
    def construct(self):
        formula = MathTex(r"\sum_{k=1}^{n} k = \frac{n(n+1)}{2}",
                          font_size=80)
        self.play(Write(formula))
        self.wait(2)
