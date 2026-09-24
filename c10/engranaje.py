from manim import *


class Engranaje(Scene):
    def construct(self):
        n = 12
        disco = Circle(radius=2)
        # Cada diente: un rectángulo girado alrededor del centro
        dientes = [
            Rectangle(width=0.5, height=0.7).move_to(2.2 * UP)
            .rotate(k * TAU / n, about_point=ORIGIN)
            for k in range(n)
        ]
        rueda = Union(disco, *dientes)
        eje = Circle(radius=0.6)
        engranaje = Difference(rueda, eje, color=GOLD,
                               fill_opacity=1, stroke_width=0)
        # Ventanas: cuatro sectores restados al disco
        for k in range(4):
            giro = k * PI / 2 + PI / 8
            ventana = AnnularSector(inner_radius=0.9,
                                    outer_radius=1.6,
                                    angle=PI / 4, start_angle=giro)
            engranaje = Difference(engranaje, ventana, color=GOLD,
                                   fill_opacity=1, stroke_width=0)
        self.add(engranaje)
