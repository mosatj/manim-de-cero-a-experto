from manim import *


class Prediccion(Scene):
    def construct(self):
        tenue = {"stroke_opacity": 0.3}
        self.add(NumberPlane(background_line_style=tenue))
        cuadrado = Square(1, color=BLUE, fill_opacity=0.5)
        cuadrado.move_to([1, 1, 0])
        cuadrado.shift(2 * RIGHT)   # centro en (3, 1)
        cuadrado.move_to(UP)        # (0, 1): olvida lo anterior
        cuadrado.shift(LEFT)        # centro en (-1, 1)
        centro = Dot(cuadrado.get_center(), color=YELLOW)
        self.add(cuadrado, centro)
        self.add(MathTex(r"(-1,\ 1)").next_to(cuadrado, UP))
