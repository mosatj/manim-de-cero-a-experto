from manim import *


class VueltaCompleta(Scene):
    def construct(self):
        izquierdo = Square(side_length=2.5, color=BLUE,
                           fill_opacity=0.6).shift(3 * LEFT)
        derecho = izquierdo.copy().shift(6 * RIGHT)
        for c in (izquierdo, derecho):
            c.add(Dot(c.get_corner(UR), color=RED))
        self.add(izquierdo, derecho,
                 Text(".animate.rotate(TAU)", font_size=30)
                 .next_to(izquierdo, DOWN),
                 Text("Rotate(c, angle=TAU)", font_size=30)
                 .next_to(derecho, DOWN))
        # El de la izquierda no se mueve: inicio y final coinciden
        self.play(izquierdo.animate.rotate(TAU),
                  Rotate(derecho, angle=TAU), run_time=3)
