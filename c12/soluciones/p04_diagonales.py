from manim import *


class Diagonales(Scene):
    def construct(self):
        n = 5
        tablero = VGroup(*[
            VGroup(*[Square(0.8) for _ in range(n)]).arrange(
                RIGHT, buff=0)
            for _ in range(n)
        ]).arrange(DOWN, buff=0)
        for i in range(n):
            tablero[i][i].set_fill(BLUE, opacity=0.7)          # una
            tablero[i][n - 1 - i].set_fill(RED, opacity=0.7)  # otra
        self.add(tablero)
