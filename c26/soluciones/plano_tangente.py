from manim import *


def f(x, y):
    return 3 - 0.3 * x**2 - 0.5 * y**2


a, b = 1, 1
fx, fy = -0.6 * a, -1.0 * b                 # derivadas parciales


class PlanoTangente(ThreeDScene):
    def construct(self):
        ejes = ThreeDAxes(x_range=[-3, 3], y_range=[-3, 3],
                          z_range=[0, 4], x_length=6, y_length=6,
                          z_length=4)
        superficie = ejes.plot_surface(
            f, u_range=[-2.5, 2.5], v_range=[-2.5, 2.5],
            resolution=(20, 20), fill_opacity=0.6,
            checkerboard_colors=[BLUE_D, BLUE_E])
        # z = f(a,b) + fx (x−a) + fy (y−b), cerca del punto
        plano = ejes.plot_surface(
            lambda x, y: f(a, b) + fx * (x - a) + fy * (y - b),
            u_range=[a - 0.9, a + 0.9], v_range=[b - 0.9, b + 0.9],
            resolution=(4, 4), fill_opacity=0.8,
            checkerboard_colors=[GOLD_D, GOLD_E])
        punto = Dot(ejes.c2p(a, b, f(a, b)), color=RED)
        self.set_camera_orientation(phi=70 * DEGREES,
                                    theta=35 * DEGREES)
        self.add(ejes, superficie, plano)
        self.add_fixed_orientation_mobjects(punto)
