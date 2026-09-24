from manim import *


class VistaPorOmision(ThreeDScene):
    def construct(self):
        ejes = ThreeDAxes()
        esfera = Sphere(radius=1.5).shift(2 * RIGHT + OUT)
        # Sin set_camera_orientation: phi = 0 y theta = -90°:
        # la cámara mira desde arriba y todo parece plano (2D)
        self.add(ejes, esfera)
        self.wait()
        # Con una orientación inclinada aparece la profundidad
        self.move_camera(phi=70 * DEGREES, theta=-45 * DEGREES)
