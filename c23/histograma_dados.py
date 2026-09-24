from manim import *


class HistogramaDados(Scene):
    def construct(self):
        rng = np.random.default_rng(2026)    # semilla fija
        dado1 = rng.integers(1, 7, 10_000)
        dado2 = rng.integers(1, 7, 10_000)
        sumas = dado1 + dado2
        caras = list(range(2, 13))
        teorica = [(6 - abs(s - 7)) / 36 for s in caras]

        grafico = BarChart(
            values=[0.001] * 11,   # casi 0: una barra nula no crece
            bar_names=[str(s) for s in caras],
            y_range=[0, 0.2, 0.05],
            x_length=9,
            y_length=4.8,
            bar_colors=[TEAL_E, TEAL_A],
            bar_fill_opacity=0.9,
        ).shift(0.5 * DOWN)
        # Probabilidad teórica: un trazo amarillo sobre cada barra
        marcas = VGroup(*[
            Line(grafico.c2p(i + 0.15, p), grafico.c2p(i + 0.85, p),
                 color=YELLOW, stroke_width=5)
            for i, p in enumerate(teorica)
        ])
        titulo = Tex(r"Suma de dos dados: frecuencia relativa",
                     font_size=40).to_edge(UP)
        rotulo_n = MathTex("n =", font_size=40)
        contador = Integer(0, font_size=40, group_with_commas=False)
        panel = VGroup(rotulo_n, contador).arrange(RIGHT)
        panel.next_to(titulo, DOWN).to_edge(RIGHT, buff=1.2)

        self.add(grafico, marcas, titulo, panel)
        for n in [10, 100, 1000, 10_000]:
            conteo = np.bincount(sumas[:n], minlength=13)[2:]
            frec = np.maximum(conteo / n, 0.001)
            self.play(
                grafico.animate.change_bar_values(frec),
                ChangeDecimalToValue(contador, n),
                run_time=1.5,
            )
            contador.set_value(n)   # valor exacto al terminar
            self.wait(0.5)
