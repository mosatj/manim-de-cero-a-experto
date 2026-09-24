from manim import *
from analisis import leer, ajuste_exponencial
from graficos import GraficoDecaimiento


class AjusteExponencial(Scene):
    def construct(self):
        rondas, quedan = leer()
        n0, k, semivida = ajuste_exponencial(rondas, quedan)
        grafico = GraficoDecaimiento(ancho=8, alto=5).shift(
            LEFT * 1.8
        )
        puntos = VGroup(
            *[grafico.punto(r, q) for r, q in zip(rondas, quedan)]
        )
        self.play(Create(grafico))
        self.play(
            LaggedStart(
                *[FadeIn(p, scale=2) for p in puntos],
                lag_ratio=0.15,
            )
        )

        curva = grafico.curva_ajuste(n0, k)
        # Los números del rótulo salen del ajuste, no de la mano
        modelo = MathTex(
            rf"N(n) \approx {n0:.0f}\,e^{{-{k:.3f}\,n}}",
            font_size=40,
        )
        modelo.to_corner(UR).shift(DOWN * 0.8)
        self.play(Create(curva), Write(modelo))

        marca = grafico.marca_semivida(n0, semivida)
        texto = MathTex(
            rf"t_{{1/2}} = \frac{{\ln 2}}{{k}} \approx "
            rf"{semivida:.2f}\ \text{{rondas}}",
            font_size=36,
        )
        texto.next_to(modelo, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Create(marca), Write(texto))
