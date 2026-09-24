import numpy as np


def mas_suave(t):                     # 6t^5 − 15t^4 + 10t^3
    return t**3 * (10 - 15 * t + 6 * t**2)


t = np.linspace(0, 1, 1001)
y = mas_suave(t)
v = np.gradient(y, t)                # velocidad (derivada numérica)
a = np.gradient(v, t)                 # aceleración
print("f(0), f(1):", y[0], y[-1])
print("velocidad en los extremos:", v[0].round(4), v[-1].round(4))
print("aceleración en los extremos:", a[1].round(3), a[-2].round(3))
print("velocidad máxima:", v.max().round(4), "en", t[v.argmax()])
print("¿siempre creciente?", np.all(np.diff(y) >= 0))
