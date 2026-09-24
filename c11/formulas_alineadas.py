from manim import *


class FormulasAlineadas(Scene):
    def construct(self):
        # & marca el punto de alineación y \\ cambia de renglón
        pasos = MathTex(
            r"2x + 3 &= 11 \\",
            r"2x &= 11 - 3 \\",
            r"2x &= 8 \\",
            r"x &= 4",
            font_size=64,
        )
        for paso in pasos:          # cada argumento es una parte
            self.play(Write(paso))
        marco = SurroundingRectangle(pasos[3], buff=0.2)
        self.play(Create(marco))
        self.wait()
