from manim import *


class IdentidadNotable(Scene):
    def construct(self):
        lineas = [
            r"(a+b)^2 - (a-b)^2",
            r"= (a^2 + 2ab + b^2) - (a^2 - 2ab + b^2)",
            r"= a^2 + 2ab + b^2 - a^2 + 2ab - b^2",
            r"= 4ab",
        ]
        pasos = VGroup(*[MathTex(t, font_size=56) for t in lineas])
        pasos.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        pasos[-1].set_color(BLUE)  # el resultado, destacado
        for paso in pasos:  # cada línea se escribe tras la anterior
            self.play(Write(paso))
            self.wait(0.5)
