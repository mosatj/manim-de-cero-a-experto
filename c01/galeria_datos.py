from manim import *


class GaleriaDatos(Scene):
    def construct(self):
        grafico = BarChart(
            values=[3.1, 4.6, 2.2, 5.4, 3.8, 4.9],
            bar_names=["L", "M", "X", "J", "V", "S"],
            y_range=[0, 6, 1], x_length=10, y_length=5.5,
            bar_colors=[BLUE, TEAL, GREEN, YELLOW, GOLD, RED],
        )
        valores = grafico.get_bar_labels(font_size=30)
        self.add(grafico, valores)
