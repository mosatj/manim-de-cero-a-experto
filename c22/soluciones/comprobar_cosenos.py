import numpy as np

rng = np.random.default_rng(2026)            # reproducible
peor = 0.0
for _ in range(10000):
    A, B, C = rng.uniform(-5, 5, size=(3, 2))
    a = np.linalg.norm(B - C)
    b = np.linalg.norm(A - C)
    c = np.linalg.norm(A - B)
    cosB = np.dot(A - B, C - B) / (c * a)
    peor = max(peor, abs(b**2 - (a**2 + c**2 - 2 * a * c * cosB)))
print(f"10 000 triángulos: mayor discrepancia = {peor:.1e}")
# Potencia del punto C respecto de la circunferencia (A, c)
B, C = np.zeros(2), np.array([6.0, 0])
A = 3 * np.array([np.cos(np.radians(50)), np.sin(np.radians(50))])
c = np.linalg.norm(A - B)
potencia = np.linalg.norm(C - A)**2 - c**2   # |CA|^2 - radio^2
F = np.array([2 * c * np.cos(np.radians(50)), 0])
print(f"potencia = {potencia:.4f},  CF*CB = "
      f"{np.linalg.norm(C - F) * np.linalg.norm(C - B):.4f}")
