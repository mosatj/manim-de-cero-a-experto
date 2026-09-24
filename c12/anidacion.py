from manim import *


class Anidacion(Scene):
    def construct(self):
        # Tablero: un grupo de filas; cada fila, un grupo de puntos
        tablero = VGroup(*[
            VGroup(*[Dot(radius=0.15) for _ in range(5)]).arrange(
                RIGHT, buff=0.6)
            for _ in range(4)
        ]).arrange(DOWN, buff=0.6)
        self.add(tablero)
        tablero[1].set_color(BLUE)          # toda la fila 1
        for i in range(4):
            tablero[i][i].set_color(YELLOW)  # la diagonal
        tablero[3][4].scale(2).set_color(RED)
        # Una rebanada de filas es otro VGroup: se mueve en bloque
        self.play(tablero[2:].animate.shift(0.5 * DOWN))
        self.wait()
