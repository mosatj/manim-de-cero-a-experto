# ¿Cómo decrece el error con n? Promedio sobre 50 semillas
import math
import sys
from pathlib import Path

CARPETA = Path(__file__).resolve().parent.parent / "proyecto7"
sys.path.insert(0, str(CARPETA))
from azar import puntos
from estimador import trayectoria

ENES = [100, 1_000, 10_000, 100_000]
SEMILLAS = range(50)
errores = {n: 0.0 for n in ENES}
for semilla in SEMILLAS:
    datos = puntos(ENES[-1], semilla)
    for n, est in zip(ENES, trayectoria(datos, ENES)):
        errores[n] += abs(est - math.pi) / len(SEMILLAS)
p = math.pi / 4
print(f"{'n':>7} {'error medio':>12} {'teórico':>9}")
for n in ENES:
    # error absoluto medio de una normal: sigma·sqrt(2/pi),
    # con sigma = 4·sqrt(p(1-p)/n)
    sigma = 4 * math.sqrt(p * (1 - p) / n)
    teorico = sigma * math.sqrt(2 / math.pi)
    print(f"{n:>7} {errores[n]:>12.4f} {teorico:>9.4f}")
print("cociente 100 -> 10 000:",
      round(errores[100] / errores[10_000], 1))
print("cociente 1000 -> 100 000:",
      round(errores[1_000] / errores[100_000], 1))
