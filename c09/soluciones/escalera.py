from manim import *


class Escalera(Scene):
    def construct(self):
        primero = Square(1, color=BLUE, fill_opacity=0.5)
        peldanos = VGroup(primero)
        for k in range(6):
            nuevo = peldanos[-1].copy()
            # Esquina con esquina: diagonal UR y sin separación
            nuevo.next_to(peldanos[-1], UR, buff=0)
            peldanos.add(nuevo)
        peldanos.set_color_by_gradient(BLUE, YELLOW)
        self.add(peldanos.move_to(ORIGIN))
