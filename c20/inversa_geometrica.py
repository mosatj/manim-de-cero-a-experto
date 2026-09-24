from manim import *

from escena_lineal import LinealScene


class InversaGeometrica(LinealScene):
    def __init__(self, **kwargs):
        super().__init__(leave_ghost_vectors=True, **kwargs)

    def construct(self):
        A = np.array([[2, 1], [5, 3]]) / 2       # det = 1/4 ≠ 0
        self.add_unit_square()
        self.add_vector([1, 1], color=YELLOW)
        rotulo = MathTex(r"A\quad\text{y luego}\quad A^{-1}")
        rotulo.add_background_rectangle().to_corner(UL)
        self.add_foreground_mobject(rotulo)
        self.play(Write(rotulo))
        self.apply_matrix(A)                      # deforma
        self.apply_inverse(A)                     # deshace
