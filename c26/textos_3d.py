from manim import *


class Textos3D(ThreeDScene):
    def construct(self):
        ejes = ThreeDAxes(x_range=[-3, 3], y_range=[-3, 3],
                          z_range=[-2, 2], x_length=6, y_length=6,
                          z_length=4)
        P = Dot3D(ejes.c2p(2, 2, 1), color=YELLOW)
        # 1) Texto «en el suelo»: gira y se deforma con la escena
        suelo = Text("plano xy", font_size=36, color=GREY_B)
        suelo.move_to(ejes.c2p(-1.5, -1.5, 0))
        # 2) Rótulo que sigue a P pero siempre mira a la cámara
        rotulo = MathTex("P", color=YELLOW)
        rotulo.move_to(ejes.c2p(2, 2, 1.6))
        # 3) Título fijo en la pantalla, como un subtítulo
        titulo = Text("Tres clases de texto", font_size=36)
        titulo.to_corner(UL)
        self.set_camera_orientation(phi=65 * DEGREES,
                                    theta=-60 * DEGREES)
        self.add(ejes, suelo, P)
        self.add_fixed_orientation_mobjects(rotulo)
        self.add_fixed_in_frame_mobjects(titulo)
        self.wait()
        self.move_camera(theta=30 * DEGREES, run_time=2)
        self.move_camera(phi=30 * DEGREES, theta=100 * DEGREES,
                         run_time=2)
