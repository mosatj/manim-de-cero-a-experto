from manim import *


class Diana(Scene):
    def construct(self):
        anillos = VGroup()
        for k in range(5):
            color = RED if k % 2 == 0 else WHITE
            anillos.add(Annulus(inner_radius=0.6 * k,
                                outer_radius=0.6 * (k + 1),
                                color=color))
        self.add(anillos, Dot(radius=0.12, color=YELLOW))
