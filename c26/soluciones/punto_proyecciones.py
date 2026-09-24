from manim import *


class PuntoProyecciones(ThreeDScene):
    def construct(self):
        ejes = ThreeDAxes(
            x_range=[0, 3], y_range=[0, 3], z_range=[0, 4],
            x_length=3, y_length=3, z_length=4)
        x, y, z = 1, 2, 3
        P = ejes.c2p(x, y, z)
        # Proyecciones sobre los planos xy, xz e yz
        pies = [ejes.c2p(x, y, 0), ejes.c2p(x, 0, z),
                ejes.c2p(0, y, z)]
        guias = VGroup(*[DashedLine(P, q, color=GREY_B)
                         for q in pies])
        marcas = VGroup(*[Dot3D(q, radius=0.05) for q in pies])
        rotulo = MathTex("P(1,2,3)", color=YELLOW, font_size=36)
        rotulo.move_to(P + 0.5 * OUT)
        self.set_camera_orientation(phi=70 * DEGREES,
                                    theta=30 * DEGREES, zoom=1.3)
        self.add(ejes, guias, marcas, Dot3D(P, color=YELLOW))
        self.add_fixed_orientation_mobjects(rotulo)
