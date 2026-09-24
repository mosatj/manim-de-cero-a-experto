from manim import *
from analisis import leer
from graficos import MallaNucleos, GraficoDecaimiento


class ExperimentoDados(Scene):
    def construct(self):
        rondas, quedan = leer()
        malla = (
            MallaNucleos().to_edge(LEFT, buff=0.5).shift(DOWN * 0.3)
        )
        grafico = GraficoDecaimiento(ancho=5.2, alto=3.8)
        grafico.to_edge(RIGHT, buff=0.5).shift(DOWN * 0.3)
        titulo = Text(
            "600 dados: en cada ronda se retiran los seises",
            font_size=30,
        ).to_edge(UP, buff=0.4)
        self.play(
            FadeIn(malla, lag_ratio=0.002),
            Write(titulo),
            Create(grafico),
        )
        contador = Text(
            f"ronda 0 · quedan {quedan[0]}", font_size=28
        )
        contador.next_to(malla, UP)
        puntos = VGroup(grafico.punto(0, quedan[0]))
        self.play(FadeIn(puntos[0]), FadeIn(contador))

        for n in range(1, 7):  # las seis primeras rondas
            nuevo = Text(
                f"ronda {n} · quedan {quedan[n]}", font_size=28
            ).move_to(contador)
            puntos.add(grafico.punto(n, quedan[n]))
            self.play(
                malla.desintegrar(quedan[n - 1] - quedan[n]),
                Transform(contador, nuevo),
                FadeIn(puntos[-1], scale=2),
                run_time=1.2,
            )
