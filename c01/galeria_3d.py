from manim import *


class Galeria3D(ThreeDScene):
    def construct(self):
        ejes = ThreeDAxes(x_range=[-3, 3], y_range=[-3, 3], z_range=[-1, 2])
        superficie = Surface(
            lambda u, v: ejes.c2p(u, v, 1.5 * np.exp(-(u**2 + v**2) / 2)),
            u_range=[-3, 3], v_range=[-3, 3], resolution=(24, 24))
        superficie.set_fill_by_value(axes=ejes, colorscale=[BLUE_E, TEAL_E,
                                                             GOLD_E, RED_E],
                                     axis=2)
        self.set_camera_orientation(phi=65 * DEGREES, theta=-50 * DEGREES,
                                    zoom=0.75)
        self.add(ejes, superficie)
