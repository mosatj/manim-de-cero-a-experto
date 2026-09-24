from manim import *


class TexMathTex(Scene):
    def construct(self):
        # Tex: modo texto; las fórmulas van entre $...$
        texto = Tex(r"El área del círculo es $A = \pi r^2$.")
        # MathTex: ya está en modo matemático (sin $)
        formula = MathTex(r"\int_0^1 x^2\,dx = \frac{1}{3}",
                          font_size=72)
        # Texto normal dentro de una fórmula: \text{...}
        mixta = MathTex(r"v = \frac{d}{t}\quad\text{(rapidez)}")
        grupo = VGroup(texto, formula, mixta).arrange(DOWN, buff=1)
        self.play(Write(texto))
        self.play(Write(formula))
        self.play(FadeIn(mixta))
        self.wait()
