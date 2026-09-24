from manim import *


class Rueda(Scene):
    def construct(self):
        n = 24
        rueda = VGroup()
        for k in range(n):
            # Tono k/n, saturación y brillo máximos
            color = ManimColor.from_hsv((k / n, 1.0, 1.0))
            rueda.add(AnnularSector(inner_radius=1.2,
                                    outer_radius=3, angle=TAU / n,
                                    start_angle=k * TAU / n,
                                    color=color))
        self.add(rueda)
