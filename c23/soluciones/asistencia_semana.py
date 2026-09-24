from manim import *


class AsistenciaSemana(Scene):
    def construct(self):
        dias = ["Lu", "Ma", "Mi", "Ju", "Vi"]
        grafico = BarChart(
            values=[28, 30, 25, 27, 22],
            bar_names=dias,
            y_range=[0, 35, 5],
            x_length=8, y_length=5,
            bar_colors=[BLUE_C, PURPLE_C],
        )
        titulo = Text("Asistencia por día", font_size=36)
        titulo.to_edge(UP)
        etiquetas = grafico.get_bar_labels(font_size=30)
        self.play(Write(titulo), Create(grafico))
        self.play(FadeIn(etiquetas))
        self.play(FadeOut(etiquetas),
                  grafico.animate.change_bar_values(
                      [31, 29, 30, 32, 27]),
                  run_time=2)
        self.play(FadeIn(grafico.get_bar_labels(font_size=30)))
        self.wait()
