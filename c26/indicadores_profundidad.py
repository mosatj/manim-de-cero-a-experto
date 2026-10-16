from manim import *


def f(x, y):
    r = np.sqrt(x**2 + y**2)
    return 1.8 * np.cos(1.6 * r) * np.exp(-0.25 * r**2)


class IndicadoresProfundidad(ThreeDScene):
    def construct(self):
        self.camera.should_apply_shading = False   # 1: sin luz
        # Luz rasante desde la izquierda: marca bien las laderas
        self.camera.light_source.move_to(9 * LEFT + 2 * OUT)
        superficie = Surface(
            lambda u, v: np.array([u, v, f(u, v)]),
            u_range=[-3, 3], v_range=[-3, 3], resolution=24,
            checkerboard_colors=False, fill_color=BLUE_E,
            fill_opacity=1, stroke_color=BLUE_E, stroke_width=0.6)
        suelo = Surface(lambda u, v: np.array([u, v, -1.6]),
                        u_range=[-4, 4], v_range=[-4, 4],
                        resolution=12,
                        checkerboard_colors=[GREY_E, GREY_D],
                        stroke_width=0)
        rotulos = [Text(t, font_size=44).to_corner(UL) for t in (
            "1. Silueta", "2. + textura", "3. + luz y sombra",
            "4. + perspectiva y suelo")]
        self.add_fixed_in_frame_mobjects(*rotulos)
        self.remove(*rotulos)
        self.set_camera_orientation(phi=68 * DEGREES,
                                    theta=-60 * DEGREES, zoom=0.9)
        self.play(FadeIn(superficie), FadeIn(rotulos[0]))
        # Gradiente de textura: las casillas lejanas se ven menores
        self.play(superficie.animate.set_fill_by_checkerboard(
                      BLUE_E, "#123044"),
                  FadeOut(rotulos[0]), FadeIn(rotulos[1]))
        self.play(FadeOut(rotulos[1]), FadeIn(rotulos[2]))
        # Luz y sombra: claras hacia la luz, oscuras de espaldas
        self.camera.should_apply_shading = True
        self.wait()
        # Convergencia, tamaño y paralaje al mover la cámara
        self.move_camera(theta=-35 * DEGREES, focal_distance=9,
                         added_anims=[FadeIn(suelo),
                                      FadeOut(rotulos[2]),
                                      FadeIn(rotulos[3])],
                         run_time=3)
