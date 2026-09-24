from manim import *


class LuzYSombra(ThreeDScene):
    def construct(self):
        esfera = Sphere(radius=1.6, resolution=(32, 16))
        esfera.set_fill_by_checkerboard(BLUE_D, BLUE_D)  # un tono
        esfera.set_stroke(width=0)
        # La luz es un Point de la cámara: va a la izquierda
        self.camera.light_source.move_to(8 * LEFT + 2 * OUT)
        self.set_camera_orientation(phi=75 * DEGREES,
                                    theta=-90 * DEGREES)
        self.add(esfera)
