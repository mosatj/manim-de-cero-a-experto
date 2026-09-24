import numpy as np

Sx = np.array([[1, 0], [0, -1]])       # refleja en el eje x
Sy = np.array([[-1, 0], [0, 1]])       # refleja en el eje y
Sd = np.array([[0, 1], [1, 0]])        # refleja en la recta y = x
p = np.array([3, 1])
print("Sx p =", Sx @ p, "| Sy p =", Sy @ p, "| Sd p =", Sd @ p)
print("Sy @ Sx =\n", Sy @ Sx, "\n(es la rotación de 180°)")
print("Sd @ Sd = identidad:", np.array_equal(Sd @ Sd, np.eye(2)))
dets = [round(np.linalg.det(M)) for M in (Sx, Sy, Sd)]
print("determinantes:", dets)
