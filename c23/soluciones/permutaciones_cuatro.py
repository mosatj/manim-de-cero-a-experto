from itertools import permutations
from manim import *


class PermutacionesCuatro(Scene):
    def construct(self):
        colores = [BLUE_D, TEAL_D, PURPLE_D, MAROON_D]
        filas = VGroup()
        # orden lexicográfico
        for p in permutations([1, 2, 3, 4]):
            filas.add(VGroup(*[
                VGroup(Square(0.45, fill_color=colores[v - 1],
                              fill_opacity=0.9, stroke_width=1.5),
                       MathTex(str(v), font_size=28))
                for v in p]).arrange(RIGHT, buff=0))
        for fila in filas:
            for celda in fila:
                celda[1].move_to(celda[0])
        # 4 columnas de 6: cada columna comparte el primer elemento
        filas.arrange_in_grid(6, 4, buff=(0.8, 0.15),
                              flow_order="dr")
        cuenta = MathTex(r"4! = 24").next_to(filas, DOWN)
        self.play(LaggedStart(*[FadeIn(f) for f in filas],
                              lag_ratio=0.1))
        self.play(Write(cuenta))
        self.wait()
