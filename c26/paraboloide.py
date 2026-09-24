from manim import *


class Paraboloide(ThreeDScene):
    def construct(self):
        ejes = ThreeDAxes(x_range=[-2, 2, 1], y_range=[-2, 2, 1],
                          z_range=[0, 5, 1], x_length=5, y_length=5,
                          z_length=4)

        def paraboloide(u, v):
            # Surface recibe (u, v) y devuelve un punto de la escena
            return ejes.c2p(u, v, u**2 + v**2)

        superficie = Surface(paraboloide, u_range=[-1.5, 1.5],
                             v_range=[-1.5, 1.5], resolution=20,
                             fill_opacity=0.8,
                             checkerboard_colors=[BLUE_D, BLUE_E])
        formula = MathTex(r"z = x^2 + y^2").to_corner(UR)
        self.add_fixed_in_frame_mobjects(formula)
        self.set_camera_orientation(phi=70 * DEGREES,
                                    theta=-60 * DEGREES)
        self.play(Create(ejes))
        self.play(Create(superficie), run_time=2)
        # Girar y, a la vez, apuntar al centro de la superficie
        self.move_camera(phi=60 * DEGREES, theta=30 * DEGREES,
                         frame_center=ejes.c2p(0, 0, 2), run_time=3)
