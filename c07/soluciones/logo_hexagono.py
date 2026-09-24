from manim import *


class LogoHexagono(Scene):
    def construct(self):
        hexagono = RegularPolygon(n=6, color=TEAL,
                                  fill_opacity=0.3)
        inicial = Text("M", font_size=80).move_to(hexagono)
        marco = SurroundingRectangle(hexagono, color=BLUE,
                                     corner_radius=0.1)
        nombre = Text("Moisés").next_to(marco, UP, buff=0.5)
        self.play(DrawBorderThenFill(hexagono),
                  Write(inicial))
        self.play(Create(marco), Write(nombre))
        logo = VGroup(hexagono, inicial, marco)
        self.play(nombre.animate.move_to(LEFT * 4),
                  logo.animate.move_to(RIGHT * 3))
        flecha = always_redraw(lambda: DoubleArrow(
            nombre.get_right(), logo.get_left(), buff=0.3))
        self.play(Create(flecha))
        self.play(Rotate(hexagono, angle=PI / 3))
        self.play(logo.animate.move_to(RIGHT * 1.5))
        self.wait()
