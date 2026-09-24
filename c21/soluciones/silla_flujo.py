from manim import *


class SillaFlujo(Scene):
    def construct(self):
        silla = lambda p: np.array([p[0], -p[1], 0]) / 2
        lineas = StreamLines(silla, x_range=[-7, 7, 0.5],
                             y_range=[-4, 4, 0.5], stroke_width=2,
                             virtual_time=4, padding=0.2)
        # Direcciones propias: se aleja por el eje x, llega por el y
        inestable = Line(7 * LEFT, 7 * RIGHT, color=RED)
        estable = Line(4 * DOWN, 4 * UP, color=BLUE)
        self.play(lineas.create())
        self.play(Create(inestable), Create(estable))
        self.add(Dot(color=WHITE))
