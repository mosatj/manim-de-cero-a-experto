# Los datos del proyecto: puntos al azar en el cuadrado unidad.
# La semilla está escrita aquí para que cualquiera pueda
# reproducir el vídeo exactamente.
import numpy as np

SEMILLA = 2026
N_TOTAL = 100_000


def puntos(n=N_TOTAL, semilla=SEMILLA):
    """n puntos uniformes en [0, 1]^2 como arreglo n x 2.
    La misma semilla produce siempre los mismos puntos."""
    rng = np.random.default_rng(semilla)
    return rng.random((n, 2))
