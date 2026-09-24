from manim import *


class ConoParametrico(ThreeDScene):
    def construct(self):
        # u: altura (0 a 2); v: ángulo; el radio crece como u/2
        propio = Surface(
            lambda u, v: np.array(
                [u / 2 * np.cos(v), u / 2 * np.sin(v), 2 - u]),
            u_range=[0, 2], v_range=[0, TAU], resolution=(8, 24),
            checkerboard_colors=[GOLD_D, GOLD_E])
        propio.shift(2.5 * LEFT + IN)
        de_manim = Cone(base_radius=1, height=2)
        de_manim.shift(2.5 * RIGHT + IN)
        self.set_camera_orientation(phi=70 * DEGREES,
                                    theta=-90 * DEGREES)
        self.add(propio, de_manim)
