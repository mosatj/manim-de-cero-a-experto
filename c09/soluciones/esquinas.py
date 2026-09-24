from manim import *


class Esquinas(Scene):
    def construct(self):
        colores = [RED, GREEN, BLUE, YELLOW]
        for esquina, color in zip([UL, UR, DL, DR], colores):
            punto = Dot(radius=0.3, color=color)
            # buff=0: el punto toca los dos bordes del marco
            self.add(punto.to_corner(esquina, buff=0))
