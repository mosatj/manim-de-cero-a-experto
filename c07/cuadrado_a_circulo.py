from manim import *


class CuadradoACirculo(Scene):
    def construct(self):
        # 1. Crear los objetos (todavía no se ven)
        cuadrado = Square(side_length=3, color=BLUE)
        circulo = Circle(radius=1.5, color=YELLOW)
        circulo.set_fill(YELLOW, opacity=0.3)

        # 2. Animar: dibujar, esperar, transformar
        self.play(Create(cuadrado))
        self.wait(1)
        self.play(Transform(cuadrado, circulo))
        self.wait(1)

        # 3. Un último gesto: desplazar la figura final
        self.play(cuadrado.animate.shift(RIGHT * 2))
        self.wait()
