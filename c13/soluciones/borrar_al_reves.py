from manim import *


class BorrarAlReves(Scene):
    def construct(self):
        lineas = VGroup(
            MathTex(r"(a+b)^2"),
            MathTex(r"= (a+b)(a+b)"),
            MathTex(r"= a^2 + 2ab + b^2"),
        ).arrange(DOWN, aligned_edge=LEFT)
        self.play(Succession(*[Write(l) for l in lineas]))
        self.wait()
        # Se borra en orden inverso: la última línea primero
        self.play(Succession(
            *[Unwrite(l) for l in reversed(lineas)]))
        self.play(Write(Text("Fin", font_size=72)))
