from manim import *
from asy_puente import importar_asy_png


def angulos_manim(x, y, z):
    """phi y theta de Manim para orthographic(x, y, z) de Asymptote:
    las dos cámaras miran desde la misma dirección."""
    r = np.sqrt(x * x + y * y + z * z)
    return np.arccos(z / r), np.arctan2(y, x)


class CamaraAsy(ThreeDScene):
    """La lámina de Asymptote junto a la superficie de Manim, vistas
    desde la misma cámara; solo la de Manim puede girar."""

    def construct(self):
        phi, theta = angulos_manim(4, 2.4, 3)  # la de asy_silla
        self.set_camera_orientation(phi=phi, theta=theta,
                                    focal_distance=200)
        lamina = importar_asy_png("asy_silla.asy", dpi=200,
                                  height=3.4)
        lamina.to_edge(LEFT, buff=0.4)
        silla = Surface(
            lambda u, v: np.array([u, v, 0.5 * (u * u - v * v)]),
            u_range=[-1.5, 1.5], v_range=[-1.5, 1.5],
            resolution=(16, 16), fill_color="#4F7C99",
            fill_opacity=0.95, stroke_color="#CFE0EA",
            stroke_width=0.6, checkerboard_colors=False,
        )
        # Derecha de la pantalla: (-sen theta, cos theta, 0)
        derecha = np.array([-np.sin(theta), np.cos(theta), 0])
        silla.shift(1.8 * derecha)
        nombre_asy = Text("Asymptote", font_size=32)
        nombre_asy.next_to(lamina, DOWN)
        nombre_manim = Text("Manim", font_size=32)
        nombre_manim.move_to(RIGHT * 2.2)
        nombre_manim.match_y(nombre_asy)
        rotulos = VGroup(nombre_asy, nombre_manim)
        self.add_fixed_in_frame_mobjects(lamina, rotulos)
        self.play(FadeIn(lamina), FadeIn(rotulos))
        self.play(Create(silla), run_time=2)
        self.move_camera(theta=theta + 70 * DEGREES, run_time=2.5)
        self.move_camera(theta=theta, run_time=2.5)
        self.wait()
