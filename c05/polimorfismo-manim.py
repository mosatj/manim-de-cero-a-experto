from manim import *


class Polimorfismo(Scene):
    def construct(self):
        figuras = VGroup(
            Circle(color=RED), Square(color=BLUE),
            Triangle(color=GREEN), Star(color=YELLOW),
        ).arrange(RIGHT, buff=1.4).set_fill(opacity=0.4)
        clases = [Create, FadeIn, GrowFromCenter,
                  DrawBorderThenFill]
        for Animacion, figura in zip(clases, figuras):
            self.play(Animacion(figura))  # misma llamada, 4 efectos
            nombre = Text(Animacion.__name__, font_size=22)
            self.add(nombre.next_to(figura, DOWN, buff=0.4))
