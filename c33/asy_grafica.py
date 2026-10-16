from manim import *
from asy_puente import importar_asy
from asy_utiles import Registro, glifos, por_color

CREMA, AZUL, GRANATE = "#E9F2F7", "#6FA3C0", "#B04A5A"


def f(x):
    return x**3 / 6 - x


def df(x):
    return x**2 / 2 - 1


class GraficaAsy(Scene):
    """Ejes de graph.asy y una tangente de Manim, encajados."""

    def construct(self):
        fig = importar_asy("asy_grafica.asy", height=6.4)
        fig.to_edge(LEFT, buff=0.3)
        a_escena = Registro(fig, (-3, -2), (3, 2))
        ejes = por_color(fig, CREMA)        # trazos y puntas
        numeros = glifos(fig).set_fill(CREMA)
        curva = por_color(fig, AZUL)
        self.play(Create(ejes), Write(numeros), run_time=2)
        self.play(Create(curva), run_time=2)

        x = ValueTracker(-2.4)

        def tangente():
            x0 = x.get_value()
            u = np.array([1, df(x0)]) / np.hypot(1, df(x0))
            c = np.array([x0, f(x0)])
            p, q = c - u, c + u
            return Line(a_escena(*p), a_escena(*q), color=GRANATE,
                        stroke_width=6)

        recta = always_redraw(tangente)
        punto = always_redraw(lambda: Dot(
            a_escena(x.get_value(), f(x.get_value())),
            color=GRANATE, radius=0.1))
        rotulo = MathTex("m = f'(x) =", font_size=44)
        valor = DecimalNumber(df(-2.4), num_decimal_places=2,
                              font_size=44)
        valor.add_updater(lambda d: d.set_value(df(x.get_value())))
        lectura = VGroup(rotulo, valor).arrange(RIGHT)
        lectura.to_corner(UR, buff=0.5)
        valor.add_updater(lambda d: d.next_to(rotulo, RIGHT))
        self.play(Create(recta), FadeIn(punto), Write(lectura))
        self.play(x.animate.set_value(2.0), run_time=5)
        self.wait()
