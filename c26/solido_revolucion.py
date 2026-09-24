from manim import *


class SolidoRevolucion(ThreeDScene):
    def construct(self):
        ejes = ThreeDAxes(
            x_range=[0, 4, 1], y_range=[-2, 2, 1],
            z_range=[-2, 2, 1],
            x_length=6, y_length=4, z_length=4)

        def punto(x, angulo):
            # (x, √x) girado un ángulo alrededor del eje x
            r = np.sqrt(x)
            y, z = r * np.cos(angulo), r * np.sin(angulo)
            return ejes.c2p(x, y, z)

        angulo = ValueTracker(0.01)
        generatriz = always_redraw(lambda: ParametricFunction(
            lambda t: punto(t, angulo.get_value()), t_range=[0, 4],
            color=YELLOW, stroke_width=5))
        solido = always_redraw(lambda: Surface(
            punto, u_range=[0, 4], v_range=[0, angulo.get_value()],
            resolution=(12, 24), fill_opacity=0.7,
            checkerboard_colors=[TEAL_D, TEAL_E], stroke_width=0.3,
            should_make_jagged=True))  # √x: tangente vertical
        volumen = MathTex(r"V=\pi\int_0^4\left(\sqrt{x}\right)^2dx"
                          r"=8\pi").to_corner(UL)
        self.set_camera_orientation(phi=70 * DEGREES,
                                    theta=-60 * DEGREES)
        self.add(ejes, solido, generatriz)
        self.play(angulo.animate.set_value(PI), run_time=3)
        self.play(angulo.animate.set_value(TAU), run_time=3)
        self.add_fixed_in_frame_mobjects(volumen)
        self.play(Write(volumen))
