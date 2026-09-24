from manim import *


class Tablas(Scene):
    def construct(self):
        # MathTable: cada entrada se compone con MathTex
        tabla = MathTable(
            [["-2", "-1", "0", "1", "2"],
             ["4", "1", "0", "1", "4"]],
            row_labels=[MathTex("x"), MathTex("x^2")],
            include_outer_lines=True,
        )
        tabla.get_row_labels().set_color(YELLOW)
        # Celdas: (fila, columna), desde 1 e incluyendo los rótulos
        tabla.add_highlighted_cell((2, 4), color=GREEN_E)
        self.play(tabla.create())
        # get_entries también usa (fila, columna)
        self.play(Indicate(tabla.get_entries((2, 4))))
        self.wait()
