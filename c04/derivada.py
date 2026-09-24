# Una función que recibe una función y devuelve otra: la derivada
import math


def derivada(f, h=1e-5):
    """Aproxima f' con el cociente (f(x+h) - f(x-h)) / (2h)."""
    def df(x):
        return (f(x + h) - f(x - h)) / (2 * h)
    return df


d_cubo = derivada(lambda x: x ** 3)
d_seno = derivada(math.sin)
for x in [0, 1, 2]:
    print(f"x = {x}: (x^3)' ≈ {d_cubo(x):.6f} (exacto {3*x**2})")
print(f"sen'(0) ≈ {d_seno(0):.8f}   cos(0) = {math.cos(0)}")
