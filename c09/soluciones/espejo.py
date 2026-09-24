from manim import *


class Espejo(Scene):
    def construct(self):
        # Recta espejo que pasa por p con dirección d (30°)
        p = np.array([0.5, -0.5, 0])
        d = rotate_vector(RIGHT, 30 * DEGREES)
        espejo = Line(p - 6 * d, p + 6 * d, color=GRAY)
        figura = Polygon([-2.5, 0.5, 0], [-0.5, 1, 0],
                         [-1.5, 2.5, 0],
                         color=BLUE, fill_opacity=0.5)
        # flip: media vuelta en torno al eje d = reflejo
        reflejo = figura.copy().set_color(YELLOW)
        reflejo.flip(d, about_point=p)
        self.add(espejo, figura, reflejo)
