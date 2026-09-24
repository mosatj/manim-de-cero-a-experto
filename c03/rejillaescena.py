from manim import *


class RejillaDePuntos(Scene):
    def construct(self):
        radio = 2.5
        puntos = VGroup()   # un «grupo»: una lista de figuras
        for y in range(-3, 4):
            for x in range(-5, 6):
                if x ** 2 + y ** 2 <= radio ** 2:
                    color = BLUE
                else:
                    color = GREY_B
                puntos.add(Dot([x, y, 0], radius=0.12, color=color))
        borde = Circle(radius=radio, color=RED)
        self.play(Create(borde))
        self.play(LaggedStart(*[FadeIn(p) for p in puntos]))
        self.wait()
