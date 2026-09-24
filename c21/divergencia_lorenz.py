import numpy as np


def lorenz(p, sigma=10.0, rho=28.0, beta=8 / 3):
    x, y, z = p
    return np.array([sigma * (y - x), x * (rho - z) - y,
                     x * y - beta * z])


def paso_rk4(F, p, h):
    k1 = F(p)
    k2 = F(p + h / 2 * k1)
    k3 = F(p + h / 2 * k2)
    k4 = F(p + h * k3)
    return p + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


h, d0 = 0.001, 1e-10
a = np.array([1.0, 1.0, 1.0])
for _ in range(20000):                 # 20 unidades de transitorio:
    a = paso_rk4(lorenz, a, h)          # a queda sobre el atractor
b = a + np.array([d0, 0, 0])              # vecino a distancia 1e-10
tiempos, distancias = [0.0], [d0]
for i in range(1, 27001):                  # t de 0 a 27
    a, b = paso_rk4(lorenz, a, h), paso_rk4(lorenz, b, h)
    if i % 3000 == 0:
        tiempos.append(i * h)
        distancias.append(np.linalg.norm(a - b))
for t, d in zip(tiempos, distancias):
    print(f"t = {t:4.0f}   |delta| = {d:.3e}")
# Ajuste log|delta| ≈ log d0 + lambda t mientras |delta| < 1
t, d = np.array(tiempos), np.array(distancias)
fase = d < 1
lam = np.polyfit(t[fase], np.log(d[fase]), 1)[0]
print(f"tasa de separación estimada: lambda ≈ {lam:.2f}")
