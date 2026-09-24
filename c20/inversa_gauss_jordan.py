from manim import *

from gauss_jordan import gauss_jordan, tex


class InversaGaussJordan(Scene):
    def construct(self):
        A = [[2, 1], [5, 3]]                          # det A = 1
        aumentada = [fila + [int(i == j) for j in range(2)]
                     for i, fila in enumerate(A)]     # [A | I]
        pasos = gauss_jordan(aumentada, columnas=2)
        estados = VGroup()
        for _, M, _ in pasos:
            mat = Matrix([[tex(x) for x in fila] for fila in M],
                         h_buff=0.9).scale(0.8)
            col = mat.get_columns()
            x = (col[1].get_right()[0] + col[2].get_left()[0]) / 2
            mat.add(Line([x, mat.get_top()[1] - 0.1, 0],
                         [x, mat.get_bottom()[1] + 0.1, 0]))
            for c in col[2:]:                     # la mitad derecha
                c.set_color(YELLOW)
            estados.add(mat)
        flechas = VGroup(*[MathTex(r"\to") for _ in estados[1:]])
        piezas = [m for par in zip(estados, flechas) for m in par]
        cadena = VGroup(*piezas, estados[-1])
        cadena.arrange_in_grid(rows=2, buff=(0.35, 0.8))
        cadena.scale_to_fit_width(13).shift(0.5 * UP)
        final = MathTex(
            r"A^{-1}=\begin{bmatrix}3&-1\\-5&2\end{bmatrix}",
            color=YELLOW).to_edge(DOWN)
        self.play(FadeIn(estados[0]))
        for f, m in zip(flechas, estados[1:]):
            self.play(Write(f), FadeIn(m, shift=0.3 * RIGHT))
        self.play(Write(final))
