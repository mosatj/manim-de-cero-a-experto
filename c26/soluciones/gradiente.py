from manim import *


def f(x, y):
    return x**2 + 2 * y**2


class Gradiente(ThreeDScene):
    def construct(self):
        ejes = ThreeDAxes(x_range=[-2.5, 2.5], y_range=[-2, 2],
                          z_range=[0, 4], x_length=5, y_length=4,
                          z_length=4)
        niveles = VGroup()
        for c in [0.5, 1.5, 3]:
            curva = ImplicitFunction(lambda x, y: f(x, y) - c,
                                     x_range=[-2.5, 2.5],
                                     y_range=[-2, 2])
            curva.apply_function(lambda p: ejes.c2p(p[0], p[1], 0))
            niveles.add(curva.set_stroke(BLUE, 3))
        # Puntos de la curva f = 3 y su gradiente (2x, 4y)
        flechas = VGroup()
        for t in np.linspace(0, TAU, 8, endpoint=False):
            x, y = np.sqrt(3) * np.cos(t), np.sqrt(1.5) * np.sin(t)
            g = np.array([2 * x, 4 * y]) * 0.18  # escala visual
            flechas.add(Arrow3D(ejes.c2p(x, y, 0),
                                ejes.c2p(x + g[0], y + g[1], 0),
                                color=RED, thickness=0.015))
        self.set_camera_orientation(phi=30 * DEGREES,
                                    theta=-90 * DEGREES, zoom=1.2)
        self.add(ejes, niveles, flechas)
