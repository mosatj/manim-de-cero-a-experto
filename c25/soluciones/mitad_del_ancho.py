from manim import *


class MitadDelAncho(MovingCameraScene):
    def construct(self):
        cuadrado = Square(side_length=2, color=BLUE).shift(3*RIGHT)
        self.add(NumberPlane(), cuadrado)
        # Marco de 4 unidades: el cuadrado (2 u) ocupa la mitad
        self.play(self.camera.frame.animate.set(width=4)
                  .move_to(cuadrado))
