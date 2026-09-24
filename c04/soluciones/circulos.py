# Propuesto: área y perímetro de círculos
import math


def area_circulo(radio):
    return math.pi * radio ** 2


def perimetro_circulo(radio):
    return 2 * math.pi * radio


print(f"{'r':>2} {'área':>8} {'perímetro':>10}")
for r in range(1, 6):
    a, p = area_circulo(r), perimetro_circulo(r)
    print(f"{r:>2} {a:>8.3f} {p:>10.3f}")
