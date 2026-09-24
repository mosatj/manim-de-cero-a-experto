from manim import *


class Discriminante(Scene):
    def construct(self):
        formula = MathTex(r"x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}",
                          font_size=96)
        self.play(Write(formula))
        # Índices leídos antes con index_labels(formula[0])
        disc = formula[0][7:13]           # b^2-4ac
        self.play(disc.animate.set_color(YELLOW))
        llave = Brace(disc, UP, color=YELLOW)
        nombre = llave.get_tex(r"\Delta\ \text{(discriminante)}")
        nombre.set_color(YELLOW)
        self.play(GrowFromCenter(llave), FadeIn(nombre, shift=DOWN))
        self.play(Circumscribe(disc, color=YELLOW))
        self.wait()
