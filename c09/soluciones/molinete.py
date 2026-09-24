from manim import *


class Molinete(Scene):
    def construct(self):
        # Baldosa: medio cuadrado 1×1 coloreado en diagonal
        mitad = Polygon([-0.5, -0.5, 0], [0.5, -0.5, 0],
                        [-0.5, 0.5, 0], stroke_width=0,
                        fill_color=BLUE, fill_opacity=1)
        baldosa = VGroup(Square(1, stroke_width=1, color=GRAY),
                         mitad)
        piezas = VGroup(*[
            baldosa.copy().rotate(-(k % 4) * PI / 2)
            for k in range(36)
        ])
        piezas.arrange_in_grid(rows=6, cols=6, buff=0)
        self.add(piezas)
