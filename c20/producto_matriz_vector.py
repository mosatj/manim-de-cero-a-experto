from manim import *


class ProductoMatrizVector(Scene):
    def construct(self):
        A = Matrix([[2, -1], [1, 1]])
        A.set_column_colors(YELLOW, BLUE)
        x = Matrix([[3], [2]])
        x.get_entries()[0].set_color(YELLOW)
        x.get_entries()[1].set_color(BLUE)
        igual = MathTex("=")
        fila1 = VGroup(A, x, igual).arrange(RIGHT)

        # A x = x1 · (columna 1) + x2 · (columna 2)
        c1 = Matrix([[2], [1]]).set_color(YELLOW)
        c2 = Matrix([[-1], [1]]).set_color(BLUE)
        x1 = MathTex("3", color=YELLOW)
        x2 = MathTex("2", color=BLUE)
        mas, igual2 = MathTex("+"), MathTex("=")
        res = Matrix([[4], [5]]).set_color(GREEN)
        combinacion = VGroup(x1, c1, mas, x2, c2, igual2, res)
        combinacion.arrange(RIGHT)
        todo = VGroup(fila1, combinacion).arrange(RIGHT)
        todo.scale_to_fit_width(13).shift(UP)
        titulo = Text("Ax es una combinación lineal de las "
                      "columnas de A", font_size=30).to_edge(UP)
        cuenta = MathTex(r"3\begin{bmatrix}2\\1\end{bmatrix}+2"
                         r"\begin{bmatrix}-1\\1\end{bmatrix}="
                         r"\begin{bmatrix}6-2\\3+2\end{bmatrix}",
                         font_size=40).next_to(todo, DOWN, buff=0.8)

        self.play(Write(titulo), FadeIn(fila1))
        self.play(TransformFromCopy(A.get_columns()[0], c1),
                  TransformFromCopy(x.get_entries()[0], x1))
        self.play(FadeIn(mas),
                  TransformFromCopy(A.get_columns()[1], c2),
                  TransformFromCopy(x.get_entries()[1], x2))
        self.play(FadeIn(igual2), FadeIn(res), Write(cuenta))
