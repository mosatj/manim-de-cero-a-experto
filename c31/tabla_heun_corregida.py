# Recalcula la tabla del TFG de Abarca (2024) antes de animarla:
# y' = y - t^2 + 1, y(0) = 0.5, paso 0.2, solución (t+1)^2 - 0.5 e^t
import math


def f(t, y):
    return y - t**2 + 1


def exacta(t):
    return (t + 1) ** 2 - 0.5 * math.exp(t)


def euler(t, y, h):
    return y + h * f(t, y)


def heun(t, y, h):
    prediccion = y + h * f(t, y)  # paso de Euler
    return y + h / 2 * (f(t, y) + f(t + h, prediccion))


def rk4(t, y, h):
    p1 = f(t, y)
    p2 = f(t + h / 2, y + h / 2 * p1)
    p3 = f(t + h / 2, y + h / 2 * p2)
    p4 = f(t + h, y + h * p3)
    return y + h / 6 * (p1 + 2 * p2 + 2 * p3 + p4)


if __name__ == "__main__":  # no se ejecuta al importar
    h = 0.2
    metodos = {"Euler": euler, "Heun": heun, "RK4": rk4}
    valores = {nombre: 0.5 for nombre in metodos}
    print(f"{'t':>4} {'Euler':>10} {'Heun':>10} {'RK4':>10}")
    for i in range(5):
        t = i * h
        errores = [abs(valores[n] - exacta(t)) for n in metodos]
        print(
            f"{t:4.1f} " + " ".join(f"{e:10.6f}" for e in errores)
        )
        for nombre, paso in metodos.items():
            valores[nombre] = paso(t, valores[nombre], h)
