from manim import *
import pandas as pd

# pandas resume la tabla; Manim dibuja el resumen
datos = pd.read_csv("py_datos.csv")
total = datos.groupby("seccion")["visitas"].sum()
media = datos.groupby("seccion")["visitas"].mean().round(1)


class BarrasPandas(Scene):
    def construct(self):
        barras = BarChart(
            values=list(total), bar_names=list(total.index),
            y_range=[0, 450, 100], y_length=5, x_length=8,
            bar_colors=[BLUE_C, GREEN_C, ORANGE],
        )
        etiquetas = barras.get_bar_labels(font_size=30)
        titulo = Text("Visitas por sección (6 semanas)",
                      font_size=30).to_edge(UP)
        self.play(Write(titulo), Create(barras))
        self.play(FadeIn(etiquetas))
        # El texto también sale de pandas: nada se escribe a mano
        lineas = [f"{s}: media {m} por semana"
                  for s, m in media.items()]
        resumen = Text("   ".join(lineas), font_size=24,
                       color=GREY_B).to_edge(DOWN)
        self.play(FadeIn(resumen))
        self.wait()
