from manim import *
from congelar import congelar


class Fundidos(Scene):
    def construct(self):
        def origen():
            return VGroup(Square(color=BLUE), Circle(color=TEAL)
                          .shift(UP + LEFT)).scale(0.55)

        def destino():
            return VGroup(Circle(color=YELLOW), Triangle(color=RED)
                          .shift(RIGHT + DOWN)).scale(0.55)

        clases = [Transform, FadeTransform, FadeTransformPieces]
        for j, clase in enumerate(clases):
            y = 2.3 - 2.4 * j
            nombre = Text(clase.__name__, font="Monospace",
                          font_size=22)
            nombre.move_to([-5.2, y, 0])
            self.add(nombre)
            for i, alfa in enumerate([0.25, 0.5, 0.75]):
                x = -1.6 + 3.3 * i
                a = origen().move_to([x - 0.4, y, 0])
                b = destino().move_to([x + 0.4, y, 0])
                congelar(self, clase(a, b), alfa)
                if j == 0:
                    rotulo = MathTex(rf"\alpha={alfa}",
                                     font_size=30)
                    self.add(rotulo.move_to([x, 3.5, 0]))
