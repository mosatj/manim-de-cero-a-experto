from manim import *


class Multiplicar(Scene):
    def construct(self):
        n = 5
        r = range(1, n + 1)
        tabla = IntegerTable(
            [[i * j for j in r] for i in r],
            row_labels=[Integer(i) for i in r],
            col_labels=[Integer(j) for j in r],
            top_left_entry=MathTex(r"\times"),
        ).scale(0.6)
        tabla.get_labels().set_color(YELLOW)
        # Cuadrados perfectos: diagonal (fila k+1, columna k+1)
        for k in range(1, n + 1):
            tabla.add_highlighted_cell((k + 1, k + 1), color=BLUE_E)
        self.add(tabla)
