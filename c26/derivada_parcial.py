from manim import *


def f(x, y):
    return 3 - 0.3 * x**2 - 0.5 * y**2


a, b = 1, 1                       # punto (a, b)
fx = -0.6 * a                     # ∂f/∂x en (a, b)


class DerivadaParcial(ThreeDScene):
    def construct(self):
        ejes = ThreeDAxes(x_range=[-3, 3, 1], y_range=[-3, 3, 1],
                          z_range=[0, 4, 1], x_length=6, y_length=6,
                          z_length=4)
        superficie = ejes.plot_surface(
            f, u_range=[-2.5, 2.5], v_range=[-2.5, 2.5],
            resolution=(20, 20), fill_opacity=0.5,
            checkerboard_colors=[BLUE_D, BLUE_E])
        # Plano vertical y = b (una Surface en x y z)
        plano = Surface(lambda u, v: ejes.c2p(u, b, v),
                        u_range=[-3, 3], v_range=[0, 4],
                        resolution=(6, 4), fill_opacity=0.15,
                        checkerboard_colors=[GREY, GREY],
                        stroke_width=0.3)
        # Traza: la curva z = f(x, b), donde el plano corta
        traza = ParametricFunction(
            lambda t: ejes.c2p(t, b, f(t, b)), t_range=[-2.5, 2.5],
            color=YELLOW, stroke_width=5)
        P = ejes.c2p(a, b, f(a, b))
        # Un Dot con orientación fija: siempre de frente y encima
        punto = Dot(P, color=RED, radius=0.1)
        # Tangente: dirección (1, 0, fx) en coordenadas de los ejes
        tangente = Line(ejes.c2p(a - 1.5, b, f(a, b) - 1.5 * fx),
                        ejes.c2p(a + 1.5, b, f(a, b) + 1.5 * fx),
                        color=RED, stroke_width=5)
        rotulo = MathTex(
            r"\frac{\partial f}{\partial x}(1,1)=-0{,}6", color=RED)
        rotulo.to_corner(UR)
        self.add_fixed_in_frame_mobjects(rotulo)
        self.add_fixed_orientation_mobjects(punto)
        self.remove(rotulo, punto)        # aparecerán más tarde
        self.set_camera_orientation(phi=70 * DEGREES,
                                    theta=-110 * DEGREES)
        self.add(ejes, superficie)

        self.play(Create(plano))                          # 1
        self.play(Create(traza), FadeIn(punto))           # 2
        self.play(Create(tangente), Write(rotulo))        # 3
        # Mirar de frente al plano y = b: la traza es una parábola
        self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES,
                         run_time=3)                      # 4
