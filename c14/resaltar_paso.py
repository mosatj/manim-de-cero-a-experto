from manim import *


class ResaltarPaso(Scene):
    def construct(self):
        lineas = MathTex(
            r"(a+b)^2 &= (a+b)(a+b)\\",
            r"&= a^2 + ab + ba + b^2\\",
            r"&= a^2 + 2ab + b^2",
        ).scale(1.2)
        self.play(Write(lineas), run_time=3)
        self.wait()
        # Énfasis pasajero: se señala sin cambiar nada
        self.play(Indicate(lineas[1], color=YELLOW,
                           scale_factor=1.1))
        self.play(Circumscribe(lineas[2], color=YELLOW))
        # Énfasis que permanece: un marco y una nota
        marco = SurroundingRectangle(lineas[2], color=YELLOW,
                                     buff=0.15)
        nota = Text("ab = ba", font_size=32, color=YELLOW)
        nota.next_to(marco, DOWN)
        self.play(Create(marco), FadeIn(nota, shift=UP))
        self.wait()
