from manim import *
from asy_puente import importar_asy
from asy_utiles import Registro, glifos, por_color

CREMA, AZUL, OCRE = "#E9F2F7", "#6FA3C0", "#E0B04A"
GRANATE, VERDE = "#B04A5A", "#7FB89A"


def f(x, y):
    return x - y


def euler(h, x=0.0, y=1.0, hasta=4.0):
    """Los puntos (x_n, y_n) del método de Euler."""
    puntos = [(x, y)]
    while x < hasta - 1e-9:
        x, y = x + h, y + h * f(x, y)
        puntos.append((x, y))
    return puntos


class ProyectoEuler(Scene):
    """Asymptote dibuja el campo y la solución; Manim, el método."""

    def construct(self):
        fig = importar_asy("asy_proyecto.asy", height=6.8)
        fig.to_edge(LEFT, buff=0.3)
        a_escena = Registro(fig, (0, 0), (4, 3.5))
        ejes, campo = por_color(fig, CREMA), por_color(fig, AZUL)
        numeros = glifos(fig).set_fill(CREMA)
        exacta = por_color(fig, OCRE)
        self.play(Create(ejes), Write(numeros), run_time=1.5)
        self.play(LaggedStart(*[Create(s) for s in campo],
                              lag_ratio=0.01), run_time=2.5)
        self.play(campo.animate.set_stroke(opacity=0.5),
                  Create(exacta), run_time=1.5)

        regla = MathTex(r"y_{n+1}=y_n+h\,f(x_n,y_n)", font_size=40)
        regla.to_corner(UR, buff=0.4)
        self.play(Write(regla))
        exacto = 4 - 1 + 2 * np.exp(-4)          # y(4) exacta
        filas = VGroup()
        for h, color in [(0.5, GRANATE), (0.25, VERDE)]:
            puntos = [a_escena(*p) for p in euler(h)]
            poligono = VMobject(color=color, stroke_width=5)
            poligono.set_points_as_corners(puntos)
            nodos = VGroup(*[Dot(p, radius=0.06, color=color)
                             for p in puntos])
            self.play(Create(poligono), LaggedStart(
                *[FadeIn(n) for n in nodos]), run_time=2.5)
            error = abs(euler(h)[-1][1] - exacto)
            fila = MathTex(rf"h={h}:\ \text{{error}}={error:.3f}",
                           font_size=38, color=color)
            filas.add(fila)
            filas.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
            filas.next_to(regla, DOWN, buff=0.6)
            filas.align_to(regla, LEFT)
            self.play(Write(fila))
        nota = Tex(r"Orden 1: error $\approx C\,h$", font_size=40)
        nota.next_to(filas, DOWN, buff=0.6).align_to(regla, LEFT)
        self.play(FadeIn(nota))
        self.wait()
