import numpy as np


def rotacion(theta):
    """Matriz 3×3 que gira un ángulo theta alrededor del eje z."""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s, 0],
                     [s, c, 0],
                     [0, 0, 1]])


if __name__ == "__main__":        # solo al ejecutar este archivo
    R = rotacion(np.pi / 2)
    print(np.round(R, 3))
    print("R @ (1, 0, 0) =", np.round(R @ [1, 0, 0], 3))

    # Muchos puntos a la vez: cada fila es un punto
    triangulo = np.array([[0, 0, 0], [2, 0, 0], [0, 1, 0]])
    print("girado 90°:\n", np.round(triangulo @ R.T, 3))
    print("¿conserva longitudes?",
          np.allclose(np.linalg.norm(triangulo, axis=1),
                      np.linalg.norm(triangulo @ R.T, axis=1)))
