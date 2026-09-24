from manim import *


class DespejeTex(Scene):
    def construct(self):
        pasos = [
            MathTex("2x", "+", "3", "=", "11"),
            MathTex("2x", "=", "11", "-", "3"),
            MathTex("2x", "=", "8"),
            MathTex("x", "=", r"\frac{8}{2}"),
            MathTex("x", "=", "4"),
        ]
        for p in pasos:
            p.scale(2.6)
        ecuacion = pasos[0]
        self.play(Write(ecuacion))
        for siguiente in pasos[1:]:
            # Las piezas con igual código TeX viajan a su sitio
            self.play(TransformMatchingTex(ecuacion, siguiente))
            ecuacion = siguiente
        marco = SurroundingRectangle(ecuacion, color=YELLOW,
                                     buff=0.25)
        self.play(Create(marco))
