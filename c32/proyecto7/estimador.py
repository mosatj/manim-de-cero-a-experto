# El modelo: cuenta puntos y estima pi. No sabe nada de Manim.
import numpy as np


def dentro(puntos):
    """Máscara lógica: True si x^2 + y^2 <= 1."""
    return (puntos**2).sum(axis=1) <= 1


def estimaciones(puntos, lotes):
    """Tras cada lote emite (n acumulado, nº dentro, estimación).
    Se detiene cuando se agotan los puntos."""
    mascara = dentro(puntos)
    n = 0
    for lote in lotes:
        n = min(n + lote, len(puntos))
        d = int(mascara[:n].sum())
        yield n, d, 4 * d / n
        if n == len(puntos):
            return


def trayectoria(puntos, enes):
    """Estimación de pi con los n primeros puntos, para cada n
    de la lista enes (sin bucles: suma acumulada)."""
    acumulado = np.cumsum(dentro(puntos))
    enes = np.asarray(enes)
    return 4 * acumulado[enes - 1] / enes
