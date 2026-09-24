from manim import *


def rotar_alrededor(puntos, theta, centro):
    """Lleva el centro al origen, gira y deshace la traslación."""
    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    return (puntos - centro) @ R.T + centro


centro = np.array([2.0, 1.0, 0.0])
cuadrado = Square().move_to(3 * RIGHT)
mios = rotar_alrededor(cuadrado.points, PI / 3, centro)
cuadrado.rotate(PI / 3, about_point=centro)     # lo que hace Manim
print("¿coinciden?", np.allclose(mios, cuadrado.points))
print("primer vértice:", np.round(mios[0], 4))
print("distancia al centro antes y después:",
      round(np.linalg.norm([4, 1, 0] - centro), 4),
      round(np.linalg.norm(mios[0] - centro), 4))
