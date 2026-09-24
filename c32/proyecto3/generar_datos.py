# Experimento de «desintegración con dados»: en cada ronda se
# lanzan los dados que quedan y se retiran los que salen 6.
# Aquí se SIMULA con una semilla fija; en clase puede hacerse
# con dados reales y el mismo CSV.
import csv
import sys

import numpy as np

N_INICIAL, RONDAS, SEMILLA = 600, 16, 31


def simular():
    rng = np.random.default_rng(SEMILLA)
    quedan, filas = N_INICIAL, [(0, N_INICIAL)]
    for ronda in range(1, RONDAS + 1):
        seises = int((rng.integers(1, 7, quedan) == 6).sum())
        quedan -= seises
        filas.append((ronda, quedan))
    return filas


filas = simular()
if "--escribir" in sys.argv:  # solo se reescribe a propósito
    with open("datos/decaimiento.csv", "w", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(["ronda", "quedan"])
        escritor.writerows(filas)
print("ronda quedan")
for ronda, quedan in filas[:6]:
    print(f"{ronda:5d} {quedan:6d}")
print(f"  ... ({len(filas)} filas en total)")
