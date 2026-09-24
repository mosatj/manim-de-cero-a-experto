from manim import *


class Tablero(Scene):
    def construct(self):
        claro, oscuro = "#EEDDBB", "#886644"
        casillas = VGroup()
        for fila in range(8):
            for col in range(8):
                color = claro if (fila + col) % 2 == 0 else oscuro
                casillas.add(Square(0.8, stroke_width=0,
                                    fill_color=color,
                                    fill_opacity=1))
        casillas.arrange_in_grid(rows=8, cols=8, buff=0)
        self.add(casillas)
