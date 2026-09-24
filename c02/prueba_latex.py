from manim import *


class PruebaLatex(Scene):
    def construct(self):
        # Si esta escena renderiza, LaTeX está bien instalado
        euler = MathTex(r"e^{i\pi} + 1 = 0", font_size=96)
        gauss = MathTex(r"\int_{-\infty}^{\infty} e^{-x^2}\,dx"
                        r" = \sqrt{\pi}", font_size=60)
        rotulo = Text("LaTeX funciona", font_size=32, color=GREEN)
        grupo = VGroup(euler, gauss, rotulo).arrange(DOWN, buff=0.6)
        self.play(Write(euler))
        self.play(Write(gauss))
        self.play(FadeIn(rotulo, shift=UP))
        self.wait()
