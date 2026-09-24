from manim import *


class ParteEntera(Scene):
    def construct(self):
        ejes = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1],
                    x_length=7, y_length=7, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 24})
        tramos = VGroup()
        for k in range(-3, 3):
            # Cada escalón es un segmento [k, k+1) a la altura k
            tramos.add(Line(ejes.c2p(k, k), ejes.c2p(k + 1, k),
                            color=BLUE, stroke_width=5))
            tramos.add(Dot(ejes.c2p(k, k), color=BLUE))  # incluido
            hueco = Circle(radius=0.08, color=BLUE, stroke_width=3)
            hueco.set_fill(BLACK, 1).move_to(ejes.c2p(k + 1, k))
            tramos.add(hueco)                             # excluido
        formula = MathTex(r"y=\lfloor x\rfloor").to_corner(UL)
        self.add(ejes, tramos, formula)
