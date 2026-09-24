from manim import *


class HeliceConica(ThreeDScene):
    def construct(self):
        # r(t) = (t cos 6t, t sin 6t, 2t): sube mientras se abre
        curva = ParametricFunction(
            lambda t: np.array(
                [t * np.cos(6 * t), t * np.sin(6 * t), 2 * t]),
            t_range=[0, 1.5], color=YELLOW).shift(1.5 * IN)
        # El cono z = 2 r contiene a la curva: vértice abajo
        cono = Surface(
            lambda u, v: np.array(
                [u * np.cos(v), u * np.sin(v), 2 * u]),
            u_range=[0, 1.5], v_range=[0, TAU], resolution=(6, 24),
            fill_opacity=0.2, checkerboard_colors=[BLUE_D, BLUE_E])
        cono.shift(1.5 * IN)
        self.set_camera_orientation(phi=70 * DEGREES,
                                    theta=-60 * DEGREES, zoom=1.4)
        self.add(cono, curva)
