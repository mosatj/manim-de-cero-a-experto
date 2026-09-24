from manim import *


class LimiteCentral(Scene):
    def construct(self):
        rng = np.random.default_rng(12)
        # 20 clases
        clases = np.linspace(1, 6, 21)
        grafico = BarChart(values=[0.001] * 20,
                           y_range=[0, 0.5, 0.1],
                           x_length=10, y_length=5,
                           bar_colors=[BLUE_D, TEAL_B],
                           bar_width=0.9)
        rotulo = MathTex(r"k = 1").to_corner(UR)
        self.add(grafico, rotulo)
        for k in [1, 2, 5, 20]:
            # 5000 medias de k dados cada una
            medias = rng.integers(1, 7, size=(5000, k)).mean(axis=1)
            conteo, _ = np.histogram(medias, bins=clases)
            self.play(grafico.animate.change_bar_values(
                np.maximum(conteo / 5000, 0.001)),
                Transform(rotulo,
                          MathTex(rf"k = {k}").to_corner(UR)),
                run_time=1.5)
        self.wait()
