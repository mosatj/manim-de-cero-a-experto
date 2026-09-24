import numpy as np


def lerp(a, b, t):
    """Interpolación lineal: t=0 da a, t=1 da b."""
    return (1 - t) * a + t * b


print("números:", [lerp(10, 20, t) for t in (0, 0.25, 0.5, 1)])
A = np.array([0.0, 0.0, 0.0])
B = np.array([4.0, 2.0, 0.0])
print("punto medio de AB:", lerp(A, B, 0.5))

# Con un arreglo de t obtenemos toda la trayectoria de una vez
t = np.linspace(0, 1, 5)[:, None]         # forma (5, 1)
print("trayectoria:\n", lerp(A, B, t))

# Colores: cada canal (rojo, verde, azul) se interpola por separado
cian = np.array([42, 143, 189])
carmesi = np.array([179, 23, 74])
for ti in (0, 0.5, 1):
    r, g, b = np.round(lerp(cian, carmesi, ti)).astype(int)
    print(f"t = {ti:<3}  color #{r:02X}{g:02X}{b:02X}")
