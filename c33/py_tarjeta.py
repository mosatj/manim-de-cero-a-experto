from pathlib import Path
from manim import *
import pandas as pd

# Una escena con «huecos»: los atributos de clase son parámetros.
# El CSV se busca junto a este archivo, se ejecute desde donde sea
DATOS = pd.read_csv(Path(__file__).with_name("py_datos.csv"))


class TarjetaSeccion(Scene):
    seccion = "A"            # la fábrica de escenas lo cambia
    color = BLUE_C

    def construct(self):
        filas = DATOS[DATOS["seccion"] == self.seccion]
        ejes = Axes(x_range=[0, 7, 1], y_range=[0, 100, 20],
                    x_length=9, y_length=4.5, tips=False)
        grafica = ejes.plot_line_graph(
            filas["semana"], filas["visitas"], line_color=self.color)
        titulo = Text(f"Sección {self.seccion}: visitas por semana",
                      font_size=32, color=self.color)
        titulo.to_edge(UP)
        total = Integer(int(filas["visitas"].sum()), font_size=40)
        total.to_corner(DR)
        self.play(Write(titulo), Create(ejes))
        self.play(Create(grafica), run_time=2)
        self.play(FadeIn(total))
        self.wait(0.5)
