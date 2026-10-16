# Comprueba el modelo sin Manim antes de animar nada
import math
import numpy as np
from azar import puntos, SEMILLA
from estimador import estimaciones, trayectoria

todos = puntos(10**6)
# 1. La misma semilla da los mismos puntos (reproducible)
assert np.array_equal(todos[:5], puntos(5))
# 2. Con un millón de puntos el error es menor que 0,01
*_, (n, d, estimacion) = estimaciones(todos, [10**6])
assert abs(estimacion - math.pi) < 0.01
print(f"semilla {SEMILLA}: {n} puntos, {d} dentro")
print(f"{'n':>9} {'estimación':>11} {'error':>9}")
enes = [10, 100, 1_000, 10_000, 100_000, 1_000_000]
for n, est in zip(enes, trayectoria(todos, enes)):
    print(f"{n:>9} {est:>11.6f} {abs(est - math.pi):>8.6f}")
