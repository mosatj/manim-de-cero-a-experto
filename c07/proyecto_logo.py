from manim import *


class ProyectoLogo(Scene):
    def construct(self):
        # Parte 1-3: círculo, marco y nombre
        circulo = Circle(radius=0.8, stroke_width=12,
                         fill_opacity=0.3, color="#34A853")
        marco = SurroundingRectangle(circulo, color=BLUE,
                                     corner_radius=0.1)
        nombre = Text("Manim", font_size=64)
        nombre.next_to(marco, UP, buff=0.5)
        self.play(Write(circulo), DrawBorderThenFill(marco),
                  Write(nombre))

        # Parte 4: agrupar y separar
        logo = VGroup(circulo, marco)
        self.play(nombre.animate.move_to(LEFT * 4.5),
                  logo.animate.move_to(RIGHT * 4))

        # Parte 5 y 7: una flecha doble que se redibuja
        flecha = always_redraw(lambda: DoubleArrow(
            nombre.get_right(), logo.get_left(), buff=0.4,
            tip_shape_start=StealthTip,
            tip_shape_end=StealthTip))
        self.play(Create(flecha))

        # Parte 6: énfasis, giro y escala
        self.play(Indicate(nombre, scale_factor=1.5,
                           color=ORANGE))
        self.play(Rotate(marco, angle=PI / 4),
                  ScaleInPlace(circulo, 2))
        self.play(logo.animate.move_to(RIGHT * 1.5))

        # Parte 8: cierre (dejamos el logo visible)
        self.play(nombre.animate.set_color("#34A853"))
        self.wait()
