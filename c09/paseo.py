from manim import *


class Paseo(Scene):
    def construct(self):
        tenue = {"stroke_opacity": 0.3}
        self.add(NumberPlane(background_line_style=tenue))
        estrella = Star(color=YELLOW, fill_opacity=0.8)
        estrella.scale(0.6)
        caja = Square(1.5, color=BLUE).move_to([3, -1, 0])
        self.add(estrella, caja)
        # Absoluto, relativo, al borde y junto a otro objeto
        self.play(estrella.animate.move_to([-4, 2, 0]))
        self.play(estrella.animate.shift(3 * DOWN))
        self.play(estrella.animate.to_corner(UR))
        self.play(estrella.animate.next_to(caja, LEFT))
