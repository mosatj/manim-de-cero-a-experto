from manim import *


class FibonacciRetrocede(MovingCameraScene):
    def construct(self):
        marco = self.camera.frame
        lados = [1, 1, 2, 3, 5, 8, 13]
        giros = [LEFT, DOWN, RIGHT, UP]
        colores = [BLUE, TEAL, GREEN, YELLOW, GOLD, RED, PURPLE]
        cuadrados = VGroup()
        marco.set(width=3)                   # empezar muy cerca
        for i, lado in enumerate(lados):
            c = Square(side_length=lado, color=colores[i],
                       fill_opacity=0.5)
            if i:
                c.next_to(cuadrados, giros[(i - 1) % 4], buff=0)
            cuadrados.add(c)
            self.play(FadeIn(c),
                      self.camera.auto_zoom([cuadrados], margin=1))
