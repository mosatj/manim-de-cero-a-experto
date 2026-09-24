import numpy as np


def koch(p, q, nivel):
    puntos = [p, q]
    for _ in range(nivel):
        nuevos = [puntos[0]]
        for a, b in zip(puntos[:-1], puntos[1:]):
            d = (b - a) / 3
            giro = np.array([[0.5, -np.sqrt(3) / 2],
                             [np.sqrt(3) / 2, 0.5]])   # +60 grados
            nuevos += [a + d, a + d + giro @ d, a + 2 * d, b]
        puntos = nuevos
    return puntos


def area(poligono):              # fórmula del cordón (shoelace)
    x, y = np.array(poligono).T
    xs, ys = np.roll(x, -1), np.roll(y, -1)
    return 0.5 * abs(np.dot(x, ys) - np.dot(y, xs))


ang = np.pi / 2 - 2 * np.pi / 3 * np.arange(3)  # triángulo horario
v = [np.array([np.cos(a), np.sin(a)]) for a in ang]
A0 = area(v)
print(" n   lados     perímetro   área/A0   fórmula")
for n in range(7):
    copo = []
    for i in range(3):
        copo += koch(v[i], v[(i + 1) % 3], n)[:-1]
    per = sum(np.linalg.norm(np.roll(copo, -1, 0) - copo, axis=1))
    formula = 8 / 5 - 3 / 5 * (4 / 9) ** n
    razon = area(copo) / A0
    print(f"{n:2d} {len(copo):7d}   {per:9.4f}   {razon:.6f}"
          f"  {formula:.6f}")
