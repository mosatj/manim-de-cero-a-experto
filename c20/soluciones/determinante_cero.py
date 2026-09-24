import sys

sys.path.insert(0, "..")
from manim import *
from escena_lineal import LinealScene


class DeterminanteCero(LinealScene):
    def construct(self):
        A = [[2, 4], [1, 2]]               # det A = 2·2 − 4·1 = 0
        self.add_unit_square()
        # (2, −1) está en el núcleo: A (2, −1) = (0, 0)
        self.add_vector([2, -1], color=YELLOW)
        self.apply_matrix(A)
