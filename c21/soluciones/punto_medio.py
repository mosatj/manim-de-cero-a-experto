import numpy as np


def heun(f, t, y, h):
    k1 = f(t, y)
    return y + h / 2 * (k1 + f(t + h, y + h * k1))


def punto_medio(f, t, y, h):
    # pendiente evaluada en el punto medio del paso
    return y + h * f(t + h / 2, y + h / 2 * f(t, y))


f = lambda t, y: y - t**2 + 1
exacta = lambda t: (t + 1)**2 - 0.5 * np.exp(t)
h = 0.2
t, yh, ym = 0.0, 0.5, 0.5
print(" t    Heun      p. medio   err Heun   err p. medio")
for _ in range(5):
    yh, ym, t = heun(f, t, yh, h), punto_medio(f, t, ym, h), t + h
    print(f"{t:.1f}  {yh:.6f}  {ym:.6f}   {abs(exacta(t) - yh):.2e}"
          f"   {abs(exacta(t) - ym):.2e}")
