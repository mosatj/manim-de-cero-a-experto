from manim import *


class Baricentro(Scene):
    def construct(self):
        A, B = np.array([-4, -2.5, 0]), np.array([4, -2.5, 0])
        angulo = ValueTracker(PI / 3)
        C = lambda: 3 * np.array([np.cos(angulo.get_value()),
                                  np.sin(angulo.get_value()), 0])
        vertices = lambda: [A, B, C()]

        def medianas():
            v = vertices()
            return VGroup(*[
                Line(v[k], (v[(k + 1) % 3] + v[(k + 2) % 3]) / 2)
                for k in range(3)]).set_stroke(YELLOW, 2)

        triangulo = always_redraw(
            lambda: Polygon(*vertices(), color=BLUE))
        lineas = always_redraw(medianas)
        G = always_redraw(
            lambda: Dot(sum(vertices()) / 3, color=RED))
        self.add(triangulo, lineas, G)
        self.play(angulo.animate.set_value(2.6), run_time=3)
