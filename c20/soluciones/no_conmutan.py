import sys

sys.path.insert(0, "..")
from manim import *
from escena_lineal import LinealScene

R = [[0, -1], [1, 0]]                         # giro de 90°
C = [[1, 1], [0, 1]]                          # cizalla


class GiroLuegoCizalla(LinealScene):          # resultado: C R
    def construct(self):
        self.add_unit_square()
        self.apply_matrix(R)
        self.apply_matrix(C)


class CizallaLuegoGiro(LinealScene):          # resultado: R C
    def construct(self):
        self.add_unit_square()
        self.apply_matrix(C)
        self.apply_matrix(R)
