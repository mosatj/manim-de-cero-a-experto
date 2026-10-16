import sys
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent  # codigo/c32
sys.path.insert(0, str(RAIZ / "proyecto6"))
from eliminacion import gauss_jordan
from sistema import AMPLIADA, COLUMNAS_A


def contar(ampliada, columnas):
    tipos = Counter(e[0] for e in gauss_jordan(ampliada, columnas))
    nombres = ("escalar", "eliminar", "intercambiar")
    return {t: tipos[t] for t in nombres}


print("sistema del proyecto:", contar(AMPLIADA, COLUMNAS_A))
# Un sistema 4x4 con todos los pivotes distintos de 1 y un cero
# en la posición del primer pivote (obliga a intercambiar)
OTRO = [
    [0, 2, 1, 1, 5],
    [2, 4, 0, 2, 10],
    [4, 2, 2, 0, 8],
    [2, 0, 4, 2, 12],
]
print("sistema 4x4:         ", contar(OTRO, 4))
