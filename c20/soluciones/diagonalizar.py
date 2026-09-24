import sys

sys.path.insert(0, "..")
from manim import *
from escena_lineal import LinealScene

P = np.array([[1, 1], [1, -1]])       # columnas: autovectores
D = np.diag([3, 1])                           # autovalores
# A = P D P^(-1): cambiar de base, estirar y volver a la base usual
class Diagonalizar(LinealScene):
    def __init__(self, **kwargs):
        super().__init__(leave_ghost_vectors=True, **kwargs)

    def construct(self):
        self.add_vector([1, 1], color=YELLOW)
        self.apply_inverse(P)
        self.apply_matrix(D)
        self.apply_matrix(P)
        texto = MathTex(
            r"PDP^{-1}=\begin{bmatrix}2&1\\1&2\end{bmatrix}")
        texto.add_background_rectangle().to_corner(UL)
        self.play(Write(texto))
