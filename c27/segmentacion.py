from manim import *


class Segmentacion(Scene):
    def construct(self):
        # Una derivación en segmentos: un solo cambio en cada paso
        pasos = [
            r"(a+b)^2",
            r"(a+b)(a+b)",
            r"a^2 + ab + ba + b^2",
            r"a^2 + 2ab + b^2",
        ]
        actual = MathTex(pasos[0], font_size=72)
        self.play(Write(actual))
        for paso in pasos[1:]:
            siguiente = MathTex(paso, font_size=72)
            animaciones = [TransformMatchingShapes(actual, siguiente)]
            if paso == pasos[-1]:  # el resultado se enmarca al llegar
                marco = SurroundingRectangle(siguiente, color=YELLOW,
                                             buff=0.25)
                animaciones.append(Create(marco))
            self.play(*animaciones)
            actual = siguiente
