from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class Rectangulos(Scene):
    def construct(self):
        cuadriculado = Rectangle(width=4, height=2.4, color=BLUE,
                                 grid_xstep=0.8, grid_ystep=0.6)
        radios = [0.8, 0.1, 0.8, 0.1]
        redondo = RoundedRectangle(corner_radius=radios, width=4,
                                   height=2.4, color=GREEN)
        vertices = [[-2, -1, 0], [2, -1.2, 0], [1, 1.2, 0],
                    [-1.5, 0.8, 0]]
        pico = Polygon(*vertices, color=YELLOW)
        suave = Polygon(*vertices, color=RED).round_corners(0.4)
        formas = VGroup(cuadriculado, redondo, pico, suave)
        formas.arrange_in_grid(rows=2, cols=2, buff=(2, 1))
        rotulos = ["grid_xstep=0.8, grid_ystep=0.6",
                   "corner_radius=[0.8, 0.1, 0.8, 0.1]",
                   "Polygon(*vertices)",
                   ".round_corners(0.4)"]
        for f, t in zip(formas, rotulos):
            self.add(Text(t, font_size=20).next_to(f, DOWN))
        self.add(formas)
