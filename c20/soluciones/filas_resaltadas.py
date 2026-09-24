from manim import *


class FilasResaltadas(Scene):
    def construct(self):
        M = IntegerMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        M.set_row_colors(BLUE, GREEN, YELLOW)
        marco = SurroundingRectangle(M.get_rows()[0], color=RED)
        self.add(M)
        self.play(Create(marco))
        for fila in M.get_rows()[1:]:
            self.play(marco.animate.become(
                SurroundingRectangle(fila, color=RED)))
        # Las columnas son otro VGroup: get_columns()
        self.play(marco.animate.become(
            SurroundingRectangle(M.get_columns()[1], color=RED)))
