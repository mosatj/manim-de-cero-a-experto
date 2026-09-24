from manim import *


def fila_de_poligonos(n, lado=0.8, **estilo):
    """VGroup con polígonos regulares de 3, 4, ..., n + 2 lados."""
    poligonos = [RegularPolygon(k, **estilo).scale(lado)
                 for k in range(3, n + 3)]
    return VGroup(*poligonos).arrange(RIGHT, buff=0.4)


class FuncionesEnManim(Scene):
    def construct(self):
        fila = fila_de_poligonos(5, color=BLUE, fill_opacity=0.3)
        fila.to_edge(UP, buff=0.8)
        curva = FunctionGraph(
            lambda x: np.sin(2 * x) * np.exp(-x ** 2 / 8),
            x_range=(-6, 6), color=YELLOW).shift(DOWN)
        self.play(Create(fila), run_time=2)
        self.play(Create(curva), rate_func=linear)
        self.wait()
