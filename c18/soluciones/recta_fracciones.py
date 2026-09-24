from manim import *


class RectaFracciones(Scene):
    def construct(self):
        recta = NumberLine(x_range=[0, 1, 1 / 8], length=11,
                           numbers_with_elongated_ticks=[0, 0.5, 1])
        # add_labels: diccionario {valor: rótulo}; aquí, MathTex
        rotulos = {k / 8: MathTex(rf"\tfrac{{{k}}}{{8}}")
                   for k in range(1, 8)}
        rotulos.update({0: MathTex("0"), 1: MathTex("1")})
        recta.add_labels(rotulos, font_size=34)
        punto = Dot(recta.n2p(3 / 8), color=YELLOW)
        self.add(recta, punto)
