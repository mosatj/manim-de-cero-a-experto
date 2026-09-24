from math import comb
from manim import *


class GaltonSesgado(Scene):
    def construct(self):
        filas, p, n = 8, 0.7, 2000
        rng = np.random.default_rng(4)
        # casilla de cada bola
        llegadas = rng.binomial(filas, p, n)
        frec = np.bincount(llegadas, minlength=filas + 1) / n
        teorica = [comb(filas, k) * p ** k * (1 - p) ** (filas - k)
                   for k in range(filas + 1)]
        grafico = BarChart(values=np.maximum(frec, 0.001).tolist(),
                           bar_names=[str(k)
                                      for k in range(filas + 1)],
                           y_range=[0, 0.35, 0.05], x_length=9,
                           y_length=5, bar_colors=[TEAL_E, TEAL_A])
        marcas = VGroup(*[
            Line(grafico.c2p(k + 0.15, q), grafico.c2p(k + 0.85, q),
                 color=YELLOW, stroke_width=5)
            for k, q in enumerate(teorica)])
        titulo = MathTex(
            r"p = 0.7:\ P(k)=\binom{8}{k}p^k(1-p)^{8-k}",
                         font_size=40).to_edge(UP)
        self.play(Create(grafico), Write(titulo))
        self.play(Create(marcas))
        self.wait()
