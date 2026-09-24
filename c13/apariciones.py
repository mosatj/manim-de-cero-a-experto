from manim import *


class Apariciones(Scene):
    def construct(self):
        circulo = Circle(radius=1.3, color=BLUE)
        estrella = Star(outer_radius=1.4, color=YELLOW,
                        fill_opacity=0.8)
        formula = MathTex(r"A = \pi r^2", font_size=72)
        VGroup(circulo, estrella, formula).arrange(RIGHT, buff=1.2)

        self.play(Create(circulo))             # traza el contorno
        self.play(DrawBorderThenFill(estrella))  # borde y relleno
        self.play(Write(formula))              # escritura a mano
