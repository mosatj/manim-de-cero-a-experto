import numpy as np

u = np.array([3.0, 4.0, 0.0])
v = np.array([4.0, -3.0, 0.0])
w = np.array([1.0, 1.0, 0.0])

print("|u| =", np.linalg.norm(u))              # longitud (norma)
print("u unitario =", u / np.linalg.norm(u))  # longitud 1
print("u · v =", np.dot(u, v), "=", u @ v)      # producto escalar
cos = (u @ w) / (np.linalg.norm(u) * np.linalg.norm(w))
angulo = np.degrees(np.arccos(cos))
print(f"ángulo entre u y w = {angulo:.2f}°")
print("u × w =", np.cross(u, w))               # producto vectorial
print("área del paralelogramo =", np.linalg.norm(np.cross(u, w)))
