from manim import *


class SillaPorAltura(ThreeDScene):
    def construct(self):
        ejes = ThreeDAxes(
            x_range=[-2, 2, 1], y_range=[-2, 2, 1],
            z_range=[-2, 2, 1],
            x_length=6, y_length=6, z_length=4)
        silla = ejes.plot_surface(
            lambda x, y: (x**2 - y**2) / 2,
            u_range=[-2, 2], v_range=[-2, 2], resolution=(24, 24),
            # (color, altura): el color codifica z con pivotes
            colorscale=[(BLUE_E, -2), (TEAL, -0.5), (WHITE, 0),
                        (GOLD, 0.5), (RED, 2)],
            stroke_width=0.3)
        formula = MathTex(r"z=\frac{x^2-y^2}{2}").to_corner(UL)
        self.add_fixed_in_frame_mobjects(formula)
        self.set_camera_orientation(phi=65 * DEGREES,
                                    theta=-45 * DEGREES)
        self.add(ejes, silla)
