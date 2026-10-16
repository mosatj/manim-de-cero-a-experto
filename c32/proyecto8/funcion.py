# La matemática de la lección, separada de la animación
# y comprobada antes de dibujar nada
import numpy as np
from scipy.integrate import quad

A, B = 0.0, 4.0  # intervalo del eje x que genera el sólido


def f(x):
    """Perfil del jarrón: el radio del sólido en cada x."""
    return 1 + 0.5 * np.sin(1.5 * x)


def volumen_exacto():
    """pi por la integral de f^2 en [A, B] (cuadratura de scipy)."""
    integral, _ = quad(lambda x: f(x) ** 2, A, B)
    return np.pi * integral


def particion(n):
    """Puntos medios x_i y anchura dx de n discos iguales."""
    dx = (B - A) / n
    return A + dx * (np.arange(n) + 0.5), dx


def volumen_discos(n):
    """Suma de los n discos pi f(x_i)^2 dx, con x_i en el centro."""
    xs, dx = particion(n)
    return float(np.sum(np.pi * f(xs) ** 2 * dx))


if __name__ == "__main__":
    exacto = volumen_exacto()
    print(f"Volumen exacto: {exacto:.6f}")
    print(f"{'n':>4}{'discos':>12}{'error':>12}")
    anterior = None
    for n in [4, 8, 16, 32, 64]:
        v = volumen_discos(n)
        error = abs(v - exacto)
        print(f"{n:>4}{v:12.6f}{error:12.6f}")
        assert anterior is None or error < anterior
        anterior = error
    print("El error decrece al duplicar n: la suma converge.")
