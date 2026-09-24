from manim import *


class EnfocarPunto(ThreeDScene):
    def construct(self):
        ejes = ThreeDAxes()
        esferas = VGroup(*[Sphere(radius=.3).move_to(p).set_color(c)
                           for p, c in [((3, 2, 1), RED),
                                        ((-3, -2, 0), BLUE),
                                        ((0, 3, -1), GREEN)]])
        mundo = VGroup(ejes, esferas)
        self.set_camera_orientation(phi=65 * DEGREES,
                                    theta=-50 * DEGREES)
        self.add(mundo)
        # En vez de frame_center (defectuoso fuera del eje z en la
        # v0.21), llevamos el objetivo al origen durante el zoom
        self.move_camera(zoom=2.5, run_time=2, added_anims=[
            mundo.animate.shift(-esferas[0].get_center())])
