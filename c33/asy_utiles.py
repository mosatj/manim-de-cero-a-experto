"""Utilidades para animar figuras de Asymptote ya importadas.

por_color(figura, color)  las partes de un color (trazo o relleno)
glifos(figura)            las letras: llegan negras y rellenas
flechas(partes)           agrupa cada flecha (astil, punta, borde)
Registro                  coordenadas de Asymptote -> escena
"""
from manim import *


def _hex(color) -> str:
    return ManimColor(color).to_hex().upper()


def _tiene_color(parte, buscado) -> bool:
    trazo = (parte.get_stroke_width() > 0
             and _hex(parte.get_stroke_color()) == buscado)
    relleno = (parte.get_fill_opacity() > 0
               and _hex(parte.get_fill_color()) == buscado)
    return trazo or relleno


def por_color(figura, color) -> VGroup:
    """Partes con ese color de trazo o de relleno, en su orden."""
    buscado = _hex(color)
    return VGroup(*[p for p in figura if _tiene_color(p, buscado)])


def glifos(figura) -> VGroup:
    """Las etiquetas de LaTeX: llegan rellenas de negro."""
    return por_color(figura, "#000000")


def flechas(partes, piezas=3) -> VGroup:
    """Cada flecha de Asymptote llega en tres partes seguidas."""
    return VGroup(*[VGroup(*partes[k:k + piezas])
                    for k in range(0, len(partes), piezas)])


class Registro:
    """Convierte coordenadas de Asymptote en puntos de la escena.

    El .asy dibuja dos marcas magenta en a y b (asy_registro.asy).
    Se vuelven invisibles, pero siguen dentro de la figura: el
    registro vale aunque luego la muevas o la escales."""

    MARCA = "#FF00FF"

    def __init__(self, figura, a, b):
        marcas = por_color(figura, self.MARCA)
        self.p, self.q = marcas[0], marcas[1]
        marcas.set_opacity(0)
        self.a, self.b = np.array(a, float), np.array(b, float)

    def __call__(self, x, y):
        p, q = self.p.get_center(), self.q.get_center()
        t = (np.array([x, y]) - self.a) / (self.b - self.a)
        d = q - p
        return p + np.array([t[0] * d[0], t[1] * d[1], 0])
