from manim import *


class OndasPorAltura(ThreeDScene):
    def construct(self):
        ejes = ThreeDAxes(
            x_range=[-3, 3], y_range=[-3, 3], z_range=[-1.5, 1.5],
            x_length=6, y_length=6, z_length=3)
        ondas = ejes.plot_surface(
            lambda x, y: np.sin(x) * np.cos(y),
            u_range=[-3, 3], v_range=[-3, 3], resolution=(24, 24),
            colorscale=[(BLUE, -1), (WHITE, 0), (RED, 1)])
        self.set_camera_orientation(phi=60 * DEGREES,
                                    theta=-40 * DEGREES)
        self.add(ejes, ondas)
