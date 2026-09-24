from manim import *


class VistasCamara(ThreeDScene):
    def construct(self):
        ejes = ThreeDAxes(x_range=[-3, 3], y_range=[-3, 3],
                          z_range=[-2, 2], x_length=6, y_length=6,
                          z_length=4)
        # Una «L» de dos prismas: cada vista la muestra distinta
        base = Prism(dimensions=[3, 1, 1], fill_color=BLUE)
        torre = Prism(dimensions=[1, 1, 2], fill_color=RED)
        base.move_to([0.5, 0, 0.5])
        torre.move_to([-0.5, 0, 2])
        self.add(ejes, base, torre)
        self.set_camera_orientation(phi=70 * DEGREES,
                                    theta=-60 * DEGREES, zoom=1.2)

        self.move_camera(phi=0, theta=-90 * DEGREES)   # planta
        self.move_camera(phi=90 * DEGREES)              # alzado
        self.move_camera(theta=0)                       # perfil
        self.move_camera(phi=70 * DEGREES, theta=-60 * DEGREES,
                         run_time=2)  # perspectiva
