from manim import *


class RotacionAmbiental(ThreeDScene):
    def construct(self):
        ejes = ThreeDAxes(x_range=[-4, 4], y_range=[-4, 4],
                          z_range=[-2, 2], x_length=8, y_length=8,
                          z_length=4)
        toro = Torus(major_radius=2, minor_radius=0.6,
                     resolution=(24, 12))
        toro.set_fill_by_checkerboard(TEAL_D, TEAL_E)
        self.set_camera_orientation(phi=65 * DEGREES,
                                    theta=-30 * DEGREES)
        self.add(ejes, toro)
        # rate en radianes por segundo: 0.3 rad/s ≈ 17°/s
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(4)
        self.stop_ambient_camera_rotation()
