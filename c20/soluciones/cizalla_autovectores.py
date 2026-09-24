import sys

sys.path.insert(0, "..")
from manim import *
from escena_lineal import LinealScene


class CizallaAutovectores(LinealScene):
    def __init__(self, **kwargs):
        super().__init__(show_basis_vectors=False,
                         leave_ghost_vectors=True, **kwargs)

    def construct(self):
        C = [[1, 1], [0, 1]]     # λ = 1 doble, un solo autovector
        for ang in np.linspace(0, PI, 8, endpoint=False):
            v = [2 * np.cos(ang), 2 * np.sin(ang)]
            color = RED if ang == 0 else YELLOW
            self.add_vector(v, color=color)
        self.apply_matrix(C)
