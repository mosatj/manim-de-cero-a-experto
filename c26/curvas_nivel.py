from manim import *


def f(x, y):
    return 3 * x * np.exp(-(x**2 + y**2) / 2)


NIVELES = [-1.5, -1, -0.5, 0.5, 1, 1.5]
ESCALA = [(BLUE_E, -1.8), (TEAL, -0.6), (WHITE, 0), (GOLD, 0.6),
          (RED, 1.8)]


class CurvasNivel(ThreeDScene):
    def construct(self):
        ejes = ThreeDAxes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            z_range=[-2, 2, 1],
            x_length=6, y_length=6, z_length=4)
        superficie = ejes.plot_surface(
            f, u_range=[-3, 3], v_range=[-3, 3], resolution=24,
            colorscale=ESCALA, fill_opacity=0.75, stroke_width=0.2)

        def curva(c, altura):
            # f(x, y) = c, hallada en el plano y subida a z = altura
            nivel = ImplicitFunction(lambda x, y: f(x, y) - c,
                                     x_range=[-3, 3],
                                     y_range=[-3, 3])
            nivel.apply_function(
                lambda p: ejes.c2p(p[0], p[1], altura))
            color = RED if c > 0 else BLUE
            return nivel.set_stroke(color, width=3)

        en_superficie = VGroup(*[curva(c, c) for c in NIVELES])
        en_el_plano = VGroup(*[curva(c, 0) for c in NIVELES])
        titulo = MathTex(r"f(x,y)=3x\,e^{-(x^2+y^2)/2}")
        titulo.to_corner(UL)
        self.add_fixed_in_frame_mobjects(titulo)
        self.set_camera_orientation(phi=65 * DEGREES,
                                    theta=-60 * DEGREES)
        self.add(ejes)

        self.play(Create(superficie), run_time=2)            # 1
        self.play(Create(en_superficie), run_time=2)         # 2
        # 3: cada curva «cae» verticalmente hasta el plano z = 0
        self.play(ReplacementTransform(en_superficie, en_el_plano),
                  superficie.animate.set_fill(opacity=0.25),
                  run_time=2)
        # 4: vista cenital: el mapa de curvas de nivel
        self.move_camera(phi=0, theta=-90 * DEGREES, run_time=3)
