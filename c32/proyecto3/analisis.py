# Análisis: leer el CSV y ajustar N(n) = N0 exp(-k n) por
# mínimos cuadrados sobre ln N (una recta). Sin Manim: se
# prueba por separado.
import csv
import math

import numpy as np


def leer(ruta="datos/decaimiento.csv"):
    with open(ruta, newline="") as f:
        filas = list(csv.DictReader(f))
    rondas = np.array([int(fila["ronda"]) for fila in filas])
    quedan = np.array([int(fila["quedan"]) for fila in filas])
    return rondas, quedan


def ajuste_exponencial(rondas, quedan):
    pendiente, corte = np.polyfit(rondas, np.log(quedan), 1)
    k = -pendiente
    return math.exp(corte), k, math.log(2) / k  # N0, k, semivida


if __name__ == "__main__":
    rondas, quedan = leer()
    n0, k, semivida = ajuste_exponencial(rondas, quedan)
    teorico = -math.log(5 / 6)  # probabilidad de sobrevivir: 5/6
    print(f"N0 ajustado  = {n0:7.1f}")
    print(f"k ajustado   = {k:7.4f}   (teórico {teorico:.4f})")
    print(
        f"semivida     = {semivida:7.2f} rondas "
        f"(teórica {math.log(2) / teorico:.2f})"
    )
