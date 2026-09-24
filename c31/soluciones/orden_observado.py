# Orden observado p = log2(e(h) / e(h/2)) para cuatro métodos
import math


def f(t, y):
    return y - t**2 + 1


def exacta(t):
    return (t + 1) ** 2 - 0.5 * math.exp(t)


def euler(t, y, h):
    return y + h * f(t, y)


def heun(t, y, h):
    return y + h / 2 * (f(t, y) + f(t + h, y + h * f(t, y)))


def punto_medio(t, y, h):
    return y + h * f(t + h / 2, y + h / 2 * f(t, y))


def rk4(t, y, h):
    p1 = f(t, y)
    p2 = f(t + h / 2, y + h / 2 * p1)
    p3 = f(t + h / 2, y + h / 2 * p2)
    p4 = f(t + h, y + h * p3)
    return y + h / 6 * (p1 + 2 * p2 + 2 * p3 + p4)


def error(paso, h):
    t, y = 0.0, 0.5
    for _ in range(round(2 / h)):
        y, t = paso(t, y, h), t + h
    return abs(y - exacta(2))


for nombre, paso in (
    ("Euler", euler),
    ("Heun", heun),
    ("Punto medio", punto_medio),
    ("RK4", rk4),
):
    ordenes = [
        math.log2(error(paso, h) / error(paso, h / 2))
        for h in (0.1, 0.05, 0.025)
    ]
    print(f"{nombre:12s}", " ".join(f"{p:5.2f}" for p in ordenes))
