import numpy as np


def lorenz(p, rho, sigma=10.0, beta=8 / 3):
    x, y, z = p
    return np.array([sigma * (y - x), x * (rho - z) - y,
                     x * y - beta * z])


def final(rho, p, h=0.005, n=20000):         # integra hasta t = 100
    for _ in range(n):
        k1 = lorenz(p, rho)
        k2 = lorenz(p + h / 2 * k1, rho)
        k3 = lorenz(p + h / 2 * k2, rho)
        k4 = lorenz(p + h * k3, rho)
        p = p + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return p


for rho in (14, 28):
    c = np.sqrt(8 / 3 * (rho - 1))            # equilibrios C±
    print(f"rho = {rho}:  C± = (±{c:.4f}, ±{c:.4f}, {rho - 1})")
    for p0 in ((1, 1, 1), (-1, -1, 1)):
        x, y, z = final(rho, np.array(p0, dtype=float))
        print(f"   desde {p0}: ({x:8.4f}, {y:8.4f}, {z:8.4f})")
