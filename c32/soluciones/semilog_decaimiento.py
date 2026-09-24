import sys
from pathlib import Path

CARPETA = Path(__file__).resolve().parent.parent / "proyecto3"
sys.path.insert(0, str(CARPETA))
from manim import *
from analisis import leer, ajuste_exponencial


class SemiLog(Scene):
    """En escala logarítmica la exponencial se vuelve una recta."""

    def construct(self):
        rondas, quedan = leer(CARPETA / "datos" / "decaimiento.csv")
        n0, k, _ = ajuste_exponencial(rondas, quedan)
        ejes = Axes(
            x_range=[0, 16, 2],
            y_range=[1, 3, 1],
            x_length=8,
            y_length=5,
            tips=False,
            y_axis_config={"scaling": LogBase()},
            axis_config={"include_numbers": True},
        )
        puntos = VGroup(
            *[
                Dot(ejes.c2p(r, q), color=YELLOW)
                for r, q in zip(rondas, quedan)
            ]
        )
        recta = ejes.plot(
            lambda n: n0 * np.exp(-k * n),
            x_range=[0, 16],
            color=RED,
        )
        self.play(
            Create(ejes), LaggedStart(*[FadeIn(p) for p in puntos])
        )
        self.play(Create(recta))
