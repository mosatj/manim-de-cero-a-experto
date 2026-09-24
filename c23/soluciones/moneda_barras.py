from manim import *


class MonedaBarras(Scene):
    def construct(self):
        rng = np.random.default_rng(8)
        tiradas = rng.integers(0, 2, 200)            # 1 = cara
        grafico = BarChart(values=[0.001, 0.001],
                           bar_names=["cara", "sello"],
                           y_range=[0, 1, 0.25], x_length=5,
                           y_length=5,
                           bar_colors=[GOLD, GREY_B])
        n_texto = Integer(0).to_corner(UR, buff=1)
        rotulo = MathTex("n=").next_to(n_texto, LEFT)
        self.add(grafico, rotulo, n_texto)
        for n in [10, 50, 200]:
            # redondeo: ver texto
            caras = round(tiradas[:n].mean(), 3)
            sellos = round(1 - caras, 3)
            nuevas = [caras, sellos]
            self.play(grafico.animate.change_bar_values(nuevas),
                      ChangeDecimalToValue(n_texto, n))
        self.add(grafico.get_bar_labels(font_size=30))
        self.wait()
