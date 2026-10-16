from manim import *
import parche_frame_center  # noqa: F401  (basta importarlo)


class CentroCorregido(ThreeDScene):
    def construct(self):
        objetivo = np.array([3, 0, 0])
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES,
                                    frame_center=objetivo)
        punto = Dot(objetivo, color=RED, radius=0.2)
        rotulo = Text("Fijo en pantalla", font_size=28)
        rotulo.to_corner(UL)
        self.add_fixed_in_frame_mobjects(rotulo)
        self.add(NumberPlane(), punto)
