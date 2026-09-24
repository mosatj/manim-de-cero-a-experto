from manim import *


def divisores(n):
    return sum(1 for d in range(1, n + 1) if n % d == 0)


class Divisores(Scene):
    def construct(self):
        ns = list(range(1, 13))
        grafico = BarChart(
            values=[divisores(n) for n in ns],
            bar_names=[str(n) for n in ns],
            y_range=[0, 6, 1], y_length=4.5, x_length=10,
            bar_colors=[BLUE_D, TEAL], bar_fill_opacity=0.85,
            x_axis_config={"font_size": 30},
            y_axis_config={"font_size": 26},
        )
        cifras = grafico.get_bar_labels(font_size=30, color=WHITE)
        titulo = Text("Número de divisores de n", font_size=32)
        titulo.to_edge(UP, buff=0.4)
        self.add(titulo, grafico)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN)
                                for b in grafico.bars],
                              lag_ratio=0.1), run_time=2)
        self.play(FadeIn(cifras))
        self.wait()
