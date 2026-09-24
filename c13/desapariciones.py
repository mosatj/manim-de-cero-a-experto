from manim import *


class Desapariciones(Scene):
    def construct(self):
        circulo = Circle(radius=1.3, color=BLUE)
        estrella = Star(outer_radius=1.4, color=YELLOW,
                        fill_opacity=0.8)
        formula = MathTex(r"A = \pi r^2", font_size=72)
        VGroup(circulo, estrella, formula).arrange(RIGHT, buff=1.2)
        self.add(circulo, estrella, formula)

        self.play(Uncreate(circulo))                  # des-dibuja
        self.play(FadeOut(estrella, shift=DOWN))      # se hunde
        self.play(Unwrite(formula))                   # des-escribe
        # Las animaciones «removedoras» sacan su objeto
        cuenta = Text(f"Objetos en escena: {len(self.mobjects)}")
        self.play(Write(cuenta))
