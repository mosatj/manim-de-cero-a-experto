"""Herramientas para depurar animaciones propias (capítulo 17)."""
from manim import *

__all__ = ["tira_de_muestras"]


def tira_de_muestras(clase, mobject, alphas=(0, 0.25, 0.5, 0.75, 1),
                     buff=0.6, **kwargs):
    """Congela `clase(mobject, **kwargs)` en varios valores alpha.

    Devuelve un VGroup con una copia del mobject por cada alpha y un
    rótulo debajo. Sirve para revisar una animación sin renderizar.
    """
    tira = VGroup()
    for a in alphas:
        copia = mobject.copy()
        anim = clase(copia, **kwargs)
        anim.begin()
        anim.interpolate(a)
        rotulo = MathTex(rf"\alpha={a:g}", font_size=30)
        tira.add(VGroup(copia, rotulo.next_to(copia, DOWN, 0.4)))
    return tira.arrange(RIGHT, buff=buff, aligned_edge=DOWN)
