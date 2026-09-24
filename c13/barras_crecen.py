from manim import *


class BarrasCrecen(Scene):
    def construct(self):
        valores = [2, 3.5, 1.5, 4.5]
        suelo = Line(5 * LEFT, 5 * RIGHT).shift(2.5 * DOWN)
        barras = VGroup(*[
            Rectangle(width=1.2, height=v, fill_opacity=0.8,
                      color=color)
            for v, color in zip(valores, [BLUE, TEAL, GREEN, RED])
        ]).arrange(RIGHT, buff=0.8, aligned_edge=DOWN)
        barras.next_to(suelo, UP, buff=0)
        eje = Arrow(suelo.get_left(), suelo.get_left() + 5.5 * UP,
                    buff=0)
        etiquetas = VGroup(*[
            MathTex(str(v)).next_to(b, UP)
            for v, b in zip(valores, barras)
        ])

        self.play(Create(suelo), GrowArrow(eje))
        # Cada barra crece desde su base (el borde inferior)
        self.play(LaggedStart(
            *[GrowFromEdge(b, DOWN) for b in barras],
            lag_ratio=0.3))
        self.play(LaggedStart(
            *[FadeIn(e, shift=0.3 * DOWN) for e in etiquetas],
            lag_ratio=0.3))
