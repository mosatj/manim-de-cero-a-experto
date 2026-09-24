from manim import *


class Mobius(ThreeDScene):
    def construct(self):
        def cinta(u, v):
            # u da la vuelta; v cruza el ancho, que gira 180°
            r = 2 + v * np.cos(u / 2)
            return np.array([r * np.cos(u), r * np.sin(u),
                             v * np.sin(u / 2)])

        superficie = Surface(cinta, u_range=[0, TAU],
                             v_range=[-0.8, 0.8],
                             resolution=(48, 6),
                             checkerboard_colors=[GOLD_D, TEAL_D])
        borde = ParametricFunction(lambda t: cinta(t, 0.8),
                                   t_range=[0, 2 * TAU], color=RED)
        self.set_camera_orientation(phi=60 * DEGREES,
                                    theta=-70 * DEGREES, zoom=1.3)
        self.add(superficie, borde)
