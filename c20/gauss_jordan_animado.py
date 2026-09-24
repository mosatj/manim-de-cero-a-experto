from manim import *

from gauss_jordan import gauss_jordan, operacion, tex

COLORES = [TEAL_A, GOLD_A, RED_A]         # una por fila: F1, F2, F3


def matriz_aumentada(M, cols_A=3):
    """Matrix de Manim con filas de color y barra antes de b."""
    mat = Matrix([[tex(x) for x in fila] for fila in M], h_buff=1.2)
    for fila, color in zip(mat.get_rows(), COLORES):
        fila.set_color(color)
    col = mat.get_columns()
    izq = col[cols_A - 1].get_right()[0]
    der = col[cols_A].get_left()[0]
    x = (izq + der) / 2
    barra = Line([x, mat.get_top()[1] - 0.15, 0],
                 [x, mat.get_bottom()[1] + 0.15, 0], stroke_width=2)
    return VGroup(mat, barra)


class GaussJordanAnimado(Scene):
    def construct(self):
        sistema = MathTex(r"\begin{cases} y-z=-1\\ 2x+y+2z=10\\"
                          r" x-y=-1\end{cases}", font_size=38)
        sistema.to_corner(UL)
        pasos = gauss_jordan([[0, 1, -1, -1], [2, 1, 2, 10],
                              [1, -1, 0, -1]], columnas=3)
        matriz = matriz_aumentada(pasos[0][1]).shift(0.3 * UP)
        filas = matriz[0].get_rows()
        rotulos = VGroup()
        for i, (fila, c) in enumerate(zip(filas, COLORES)):
            r = MathTex(f"F_{i + 1}", color=c)
            r.next_to(matriz, LEFT, buff=0.5).set_y(fila.get_y())
            rotulos.add(r)
        op = MathTex("").next_to(matriz, DOWN, buff=0.6)
        marco = SurroundingRectangle(matriz).set_stroke(opacity=0)

        self.play(Write(sistema), FadeIn(matriz), FadeIn(rotulos))
        for operac, M, pivote in pasos[1:]:
            nueva = matriz_aumentada(M).move_to(matriz)
            nueva_op = MathTex(operacion(operac, latex=True),
                               color=YELLOW)
            nueva_op.next_to(nueva, DOWN, buff=0.6)
            if pivote:                    # resalta el pivote activo
                i, j = pivote
                entrada = nueva[0].get_rows()[i][j]
                nuevo_marco = SurroundingRectangle(
                    entrada, color=GREEN, buff=0.1)
            else:
                nuevo_marco = marco.copy().set_stroke(opacity=0)
            self.play(Transform(matriz, nueva),
                      Transform(op, nueva_op),
                      Transform(marco, nuevo_marco), run_time=1.2)
        solucion = MathTex(r"(x,\,y,\,z)=(1,\,2,\,3)", color=GREEN)
        solucion.next_to(op, DOWN, buff=0.5)
        self.play(Write(solucion))
