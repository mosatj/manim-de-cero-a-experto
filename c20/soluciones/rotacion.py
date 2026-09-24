import sys

sys.path.insert(0, "..")          # para importar escena_lineal
from manim import *
from escena_lineal import LinealScene


class Rotacion(LinealScene):
    def __init__(self, **kwargs):
        super().__init__(leave_ghost_vectors=True, **kwargs)

    def construct(self):
        R = [[0, -1], [1, 0]]            # giro de 90° antihorario
        self.add_vector([2, 1], color=YELLOW)
        self.apply_matrix(R)
