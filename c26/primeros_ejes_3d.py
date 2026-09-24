from manim import *


class PrimerosEjes3D(ThreeDScene):
    def construct(self):
        ejes = ThreeDAxes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            z_range=[-2, 3, 1],
            x_length=6, y_length=6, z_length=5)
        P = ejes.c2p(2, 1, 2)                     # punto P(2, 1, 2)
        pie = ejes.c2p(2, 1, 0)  # su sombra en z = 0
        guias = VGroup(
            DashedLine(ejes.c2p(2, 0, 0), pie),
            DashedLine(ejes.c2p(0, 1, 0), pie),
            DashedLine(pie, P)).set_color(GREY_B)
        punto = Dot3D(P, radius=0.1, color=YELLOW)
        # phi: inclinación desde el eje z; theta: giro en torno a z
        self.set_camera_orientation(phi=70 * DEGREES,
                                    theta=-50 * DEGREES, zoom=1.1)
        self.add(ejes, guias, punto)
        # Rótulos de los ejes que siempre miran a la cámara
        for nombre, eje in zip("xyz", ejes.get_axes()):
            rotulo = MathTex(nombre).move_to(eje.get_end() * 1.12)
            self.add_fixed_orientation_mobjects(rotulo)
