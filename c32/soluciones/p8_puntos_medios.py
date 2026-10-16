import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent  # codigo/c32
sys.path.insert(0, str(RAIZ / "proyecto8"))
import numpy as np
from funcion import f, A, B, volumen_exacto, volumen_discos


def volumen_izquierda(n):
    """Discos con el radio tomado en el extremo izquierdo."""
    dx = (B - A) / n
    xs = A + dx * np.arange(n)
    return float(np.sum(np.pi * f(xs) ** 2 * dx))


exacto = volumen_exacto()
print(f"{'n':>4}{'medio':>12}{'izquierda':>12}")
for n in [4, 8, 16, 32]:
    e_medio = abs(volumen_discos(n) - exacto)
    e_izq = abs(volumen_izquierda(n) - exacto)
    print(f"{n:>4}{e_medio:12.5f}{e_izq:12.5f}")
