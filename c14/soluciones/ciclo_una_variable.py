from manim import *


class CicloUnaVariable(Scene):
    def construct(self):
        figura = Circle(radius=1.5, color=BLUE, fill_opacity=0.5)
        destinos = [
            Square(side_length=3, color=TEAL, fill_opacity=0.5),
            Triangle(color=YELLOW, fill_opacity=0.5).scale(2),
            Star(outer_radius=1.8, color=RED, fill_opacity=0.5),
        ]
        self.play(Create(figura))
        for destino in destinos:
            # Siempre se transforma la misma variable: «figura»
            self.play(Transform(figura, destino))
        self.wait()
