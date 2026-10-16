from manim import *
import matplotlib
matplotlib.use("Agg")      # sin ventana: solo dibuja en memoria
import matplotlib.pyplot as plt
import pandas as pd


def figura_matplotlib():
    """Devuelve la figura como matriz RGBA (alto x ancho x 4)."""
    datos = pd.read_csv("py_datos.csv")
    tabla = datos.pivot(index="semana", columns="seccion",
                        values="visitas")
    plt.style.use("dark_background")   # a juego con Manim
    fig, ax = plt.subplots(figsize=(6, 4), dpi=150)
    tabla.plot(ax=ax, marker="o")
    ax.set_xlabel("semana"); ax.set_ylabel("visitas")
    ax.grid(alpha=0.3); fig.tight_layout()
    fig.canvas.draw()
    return np.asarray(fig.canvas.buffer_rgba())


class FiguraMatplotlib(Scene):
    def construct(self):
        imagen = ImageMobject(figura_matplotlib())
        imagen.height = 5.2
        imagen.shift(RIGHT * 1.6)
        marco = SurroundingRectangle(imagen, color=GREY_B, buff=0)
        titulo = Text("Una figura de matplotlib dentro de Manim",
                      font_size=30).to_edge(UP)
        self.play(Write(titulo))
        self.play(FadeIn(imagen, scale=0.9), Create(marco))
        flecha = Arrow(LEFT * 6.3, imagen.get_left(), color=ORANGE,
                       buff=0.1)
        nota = Text("ImageMobject(array)", font_size=24,
                    color=ORANGE).next_to(flecha, UP, buff=0.1)
        nota.align_to(flecha, LEFT)
        self.play(GrowArrow(flecha), FadeIn(nota))
        self.wait()
