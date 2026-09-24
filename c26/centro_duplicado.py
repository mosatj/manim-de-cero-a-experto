from manim import *


class CentroDuplicado(ThreeDScene):
    def construct(self):
        objetivo = np.array([3, 0, 0])
        # Vista cenital con el centro del encuadre en (3, 0, 0):
        # se esperaría el punto rojo en el centro de la imagen
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES,
                                    frame_center=objetivo)
        punto = Dot(objetivo, color=RED, radius=0.2)
        self.add(NumberPlane(), punto)
