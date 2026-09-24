# Propuesto: componer dos funciones
import math


def componer(f, g):
    """Devuelve la función x -> f(g(x))."""
    return lambda x: f(g(x))


raiz_de_abs = componer(math.sqrt, abs)
print(raiz_de_abs(-16))
seno_del_doble = componer(math.sin, lambda x: 2 * x)
print(round(seno_del_doble(math.pi / 4), 6))
cuadrado_mas_uno = componer(lambda y: y + 1, lambda x: x ** 2)
print([cuadrado_mas_uno(x) for x in range(4)])
