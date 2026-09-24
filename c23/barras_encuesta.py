from manim import *


class BarrasEncuesta(Scene):
    def construct(self):
        titulo = Text("Aprobados por sección", font_size=38)
        titulo.to_edge(UP)
        antes = [12, 15, 9, 17]
        despues = [16, 18, 14, 19]
        grafico = BarChart(
            values=antes.copy(),   # copia (ver el texto)
            bar_names=["A", "B", "C", "D"],
            y_range=[0, 20, 5],
            x_length=7,
            y_length=4.5,
            bar_colors=[BLUE_D, TEAL_C],
            bar_fill_opacity=0.85,
        ).shift(0.5 * DOWN)
        etiquetas = grafico.get_bar_labels(font_size=34)

        self.play(Write(titulo))
        self.play(Create(grafico), run_time=2)
        self.play(FadeIn(etiquetas, shift=0.2 * UP))
        self.wait()

        subtitulo = Text("tras el reforzamiento", font_size=28,
                         color=YELLOW).next_to(titulo, DOWN)
        self.play(
            FadeIn(subtitulo),
            FadeOut(etiquetas),
            grafico.animate.change_bar_values(despues),
            run_time=2,
        )
        self.play(FadeIn(grafico.get_bar_labels(font_size=34)))
        self.wait()
