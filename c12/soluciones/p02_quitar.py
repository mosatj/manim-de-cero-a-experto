from manim import *


class Quitar(Scene):
    def construct(self):
        fila = VGroup(*[Square(side_length=1) for _ in range(6)])
        fila.arrange(RIGHT, buff=0.3)
        self.add(fila)
        impares = fila[1::2]         # rebanada con paso: 1, 3, 5
        self.play(impares.animate.set_fill(RED, opacity=0.6))
        for cuadro in impares:
            fila -= cuadro       # sale del grupo, no de la escena
        self.play(fila.animate.arrange(RIGHT, buff=0.3).shift(DOWN),
                  FadeOut(impares))
        self.wait()
