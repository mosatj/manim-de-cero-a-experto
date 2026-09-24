from manim import *


def resaltar(mobject, color=YELLOW):
    """Devuelve Indicate seguido de Circumscribe."""
    return Succession(Indicate(mobject, color=color),
                      Circumscribe(mobject, color=color))


class ResaltarFuncion(Scene):
    def construct(self):
        formula = MathTex("a^2", "+", "b^2", "=", "c^2",
                          font_size=96)
        self.add(formula)
        # La misma función sirve para cualquier término
        for termino, color in zip(formula[::2], (BLUE, TEAL, RED)):
            self.play(resaltar(termino, color))
        self.play(formula[4].animate.set_color(RED))
