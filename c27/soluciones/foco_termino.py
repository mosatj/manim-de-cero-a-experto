from manim import *


class FocoTermino(Scene):
    def construct(self):
        formula = MathTex(r"f(x)", "=", r"a x^2", "+", r"b x", "+", "c",
                          font_size=80)
        self.play(Write(formula))
        self.wait()
        foco = formula[4]  # el término lineal
        resto = VGroup(*[m for m in formula if m is not foco])
        self.play(resto.animate.fade(0.7),
                  foco.animate.set_color(ORANGE))
        llave = Brace(foco, DOWN, color=ORANGE)
        nota = llave.get_text("inclina la parábola").set_color(ORANGE)
        self.play(GrowFromCenter(llave), FadeIn(nota))
