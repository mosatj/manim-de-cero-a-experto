from manim import *

from escena_lineal import LinealScene


class Cizalla(LinealScene):
    def __init__(self, **kwargs):
        super().__init__(show_coordinates=True,
                         leave_ghost_vectors=True, **kwargs)

    def construct(self):
        A = [[1, 1], [0, 1]]                   # cizalla horizontal
        rotulo = Matrix(A).set_column_colors(GREEN, RED)
        rotulo.add_background_rectangle().to_corner(UL)
        self.add_foreground_mobject(rotulo)       # no se deforma
        v = self.add_vector([1, 2], color=YELLOW)
        self.play(Write(rotulo))
        self.apply_matrix(A)                   # (1, 2) -> (3, 2)
        imagen = MathTex(r"A\begin{bmatrix}1\\2\end{bmatrix}="
                         r"\begin{bmatrix}3\\2\end{bmatrix}",
                         color=YELLOW).add_background_rectangle()
        imagen.next_to(v.get_end(), RIGHT)
        self.play(Write(imagen))
