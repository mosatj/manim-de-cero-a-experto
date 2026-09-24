import sys

sys.path.insert(0, "..")
from gauss_jordan import gauss_jordan

# x + 2y + z = 4,  2x + 4y + 3z = 9,  x + 2y + 2z = 5
aumentada = [[1, 2, 1, 4], [2, 4, 3, 9], [1, 2, 2, 5]]
forma = gauss_jordan(aumentada, columnas=3)[-1][1]
print("Forma escalonada reducida:")
for fila in forma:
    print("   ", "  ".join(f"{str(x):>3}" for x in fila))
