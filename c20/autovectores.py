from manim import *

from escena_lineal import LinealScene


class Autovectores(LinealScene):
    def __init__(self, **kwargs):
        super().__init__(show_basis_vectors=False,
                         leave_ghost_vectors=True, **kwargs)

    def construct(self):
        A = [[2, 1], [1, 2]]
        # Rectas de los autovectores: A las lleva en sí mismas
        for d in ([1, 1, 0], [1, -1, 0]):
            d = np.array(d)
            recta = Line(-8 * d, 8 * d, color=RED, stroke_width=2)
            self.add_transformable_mobject(recta)
        u1 = self.add_vector([1, 1], color=RED)      # λ = 3
        u2 = self.add_vector([1, -1], color=RED)     # λ = 1
        otros = [self.add_vector(v, color=YELLOW)
                 for v in ([1, 0], [0, 1], [-1, 0.5])]
        rotulo = MathTex(r"A=\begin{bmatrix}2&1\\1&2\end{bmatrix}")
        rotulo.add_background_rectangle().to_corner(UL)
        self.add_foreground_mobject(rotulo)
        self.wait(0.5)
        self.apply_matrix(A)
        valores = MathTex(
            r"A\vec u_1=3\vec u_1\qquad A\vec u_2=\vec u_2",
            color=RED).add_background_rectangle()
        valores.to_corner(UR)
        self.play(Write(valores))
