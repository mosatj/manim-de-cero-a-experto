from manim import *


def f(x):
    return 1 / (x - 1) + 1


class Asintotas(Scene):
    def construct(self):
        ejes = Axes(x_range=[-4, 6, 1], y_range=[-3, 5, 1],
                    x_length=9, y_length=6.5, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 24})
        # Dos ramas: cada x_range termina donde f sale del rango y
        # (f = -3 en x = 0.75 y f = 5 en x = 1.25)
        izquierda = ejes.plot(f, x_range=[-4, 0.75], color=BLUE)
        derecha = ejes.plot(f, x_range=[1.25, 6], color=BLUE)
        vertical = DashedLine(ejes.c2p(1, -3), ejes.c2p(1, 5),
                              color=GRAY)
        horizontal = DashedLine(ejes.c2p(-4, 1), ejes.c2p(6, 1),
                                color=GRAY)
        et_v = MathTex("x=1", font_size=32, color=GRAY_B)
        et_v.next_to(ejes.c2p(1, -3), RIGHT, buff=0.15)
        et_h = MathTex("y=1", font_size=32, color=GRAY_B)
        et_h.next_to(ejes.c2p(-4, 1), UP, buff=0.15)
        formula = MathTex(r"f(x)=\frac{1}{x-1}+1", color=BLUE)
        formula.move_to(ejes.c2p(3.8, 3.5))
        self.add(ejes, vertical, horizontal, et_v, et_h)
        self.play(Create(izquierda), Create(derecha), run_time=2)
        self.play(Write(formula))
        self.wait()
