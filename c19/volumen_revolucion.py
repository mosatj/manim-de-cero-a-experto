from manim import *


class VolumenRevolucion(ThreeDScene):
    def construct(self):
        # 1,2 unidades de pantalla por unidad en los tres ejes
        ejes = ThreeDAxes(x_range=[0, 4.5, 1],
                          y_range=[-2.5, 2.5, 1],
                          z_range=[-2.5, 2.5, 1], x_length=5.4,
                          y_length=6, z_length=6)
        self.set_camera_orientation(phi=70 * DEGREES,
                                    theta=-80 * DEGREES)
        r = lambda x: np.sqrt(max(x, 0))     # radio del disco: √x
        perfil = ejes.plot(r, x_range=[0, 4], color=YELLOW)
        region = ejes.get_area(perfil, x_range=[0, 4], color=YELLOW,
                               opacity=0.4)
        # Sólido: y = √x gira alrededor del eje x. Con s = √x
        # (x = s²) la superficie es suave también en el vértice
        solido = Surface(
            lambda s, v: ejes.c2p(s**2, s*np.cos(v), s*np.sin(v)),
            u_range=[0, 2], v_range=[0, TAU], resolution=(16, 32),
            checkerboard_colors=[BLUE_D, BLUE_E], fill_opacity=0.55,
            stroke_width=0.3)
        # Un disco representativo en x = 2: radio √2, grosor Δx
        unidad = ejes.get_x_unit_size()
        disco = Cylinder(radius=r(2) * unidad, height=0.25 * unidad,
                         direction=RIGHT, fill_color=RED,
                         fill_opacity=0.9,
                         checkerboard_colors=False)
        disco.move_to(ejes.c2p(2, 0, 0))
        formula = MathTex(r"V=\pi\int_0^4(\sqrt{x})^2\,dx=8\pi",
                          font_size=40).to_corner(UR)
        self.add_fixed_in_frame_mobjects(formula)
        self.remove(formula)

        self.play(Create(ejes), Create(perfil), FadeIn(region))
        self.play(Create(solido), run_time=2)
        self.play(FadeIn(disco))
        self.play(Write(formula))
