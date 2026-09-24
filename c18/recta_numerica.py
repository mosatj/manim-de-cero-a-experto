from manim import *


class RectaNumerica(Scene):
    def construct(self):
        # Recta de enteros: una marca y un número por unidad
        enteros = NumberLine(x_range=[-4, 4, 1], length=11,
                             include_numbers=True, font_size=30)
        enteros.shift(UP * 1.5)
        # Recta de décimas: marcas cada 0.1, números solo en algunas
        decimas = NumberLine(
            x_range=[2, 4, 0.1], length=11, font_size=30,
            numbers_to_include=[2, 2.5, 3, 3.5, 4],
            numbers_with_elongated_ticks=[2, 2.5, 3, 3.5, 4],
            decimal_number_config={"num_decimal_places": 1})
        decimas.shift(DOWN * 1.5)
        # number_to_point (n2p) traduce un número a un punto
        punto = Dot(enteros.n2p(PI), color=YELLOW)
        rotulo = MathTex(r"\pi", color=YELLOW).next_to(punto, UP)
        punto2 = Dot(decimas.n2p(PI), color=YELLOW)
        rotulo2 = MathTex(r"\pi\approx 3.14", color=YELLOW)
        rotulo2.next_to(punto2, UP)
        # Una lupa: el tramo [2, 4] de arriba se amplía abajo
        guias = VGroup(
            DashedLine(enteros.n2p(2), decimas.n2p(2)),
            DashedLine(enteros.n2p(4), decimas.n2p(4)),
        ).set_stroke(GRAY, 1.5)
        self.add(enteros, decimas, guias)
        self.play(FadeIn(punto, rotulo, punto2, rotulo2))
        self.wait()
