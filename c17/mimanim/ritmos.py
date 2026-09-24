"""Funciones de ritmo propias de mimanim (capítulo 17)."""
from manim import *
from manim.utils.rate_functions import unit_interval

__all__ = ["escalones", "pasarse_y_volver"]


@unit_interval                      # fuera de [0, 1] devuelve 0 o 1
def escalones(t, n=4):
    """Avanza a saltos: n mesetas unidas por tramos suaves."""
    k = min(int(t * n), n - 1)      # tramo actual
    return (k + smooth(t * n - k)) / n


def pasarse_y_volver(t):
    """Se pasa de la meta cerca de un 18 % y regresa."""
    return smooth(t) + 0.6 * np.sin(PI * t) * t ** 2
