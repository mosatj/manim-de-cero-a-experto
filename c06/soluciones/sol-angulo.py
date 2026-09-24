import numpy as np


def angulo(u, v):
    """Ángulo entre dos vectores, en grados."""
    cos = (u @ v) / (np.linalg.norm(u) * np.linalg.norm(v))
    return np.degrees(np.arccos(np.clip(cos, -1, 1)))


pares = [([1, 0, 0], [0, 1, 0]), ([1, 1, 0], [1, 0, 0]),
         ([2, 1, 0], [-1, 2, 0]), ([1, 2, 3], [-1, -2, -3])]
for u, v in pares:
    u, v = np.array(u), np.array(v)
    print(f"{u} y {v}: {angulo(u, v):6.2f}°",
          "(perpendiculares)" if np.isclose(u @ v, 0) else "")
