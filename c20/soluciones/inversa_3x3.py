import sys

sys.path.insert(0, "..")          # módulo gauss_jordan de c20
from gauss_jordan import gauss_jordan, operacion

A = [[1, 2, 0], [0, 1, 1], [1, 0, 1]]
aumentada = [fila + [int(i == j) for j in range(3)]
             for i, fila in enumerate(A)]           # [A | I]
pasos = gauss_jordan(aumentada, columnas=3)
for op, _, _ in pasos[1:]:
    print(operacion(op))
final = pasos[-1][1]
print("A^(-1) =")
for fila in final:
    print("   ", "  ".join(f"{str(x):>5}" for x in fila[3:]))
