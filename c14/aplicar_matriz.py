from manim import *


class AplicarMatriz(Scene):
    def construct(self):
        plano = NumberPlane(
            x_range=[-8, 8], y_range=[-5, 5],
            background_line_style={"stroke_opacity": 0.5})
        cuadrado = Square(side_length=1, color=YELLOW,
                          fill_opacity=0.6)
        cuadrado.move_to([0.5, 0.5, 0])   # el cuadrado unidad
        escena = VGroup(plano, cuadrado)

        self.play(Create(plano), FadeIn(cuadrado))
        # Cizalla: el eje x queda fijo, el eje y se inclina
        self.play(ApplyMatrix([[1, 1], [0, 1]], escena))
        # Estiramiento vertical: el área se multiplica por 2
        self.play(ApplyMatrix([[1, 0], [0, 2]], escena))
