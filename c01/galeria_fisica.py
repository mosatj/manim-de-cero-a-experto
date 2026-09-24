from manim import *


class GaleriaFisica(Scene):
    def construct(self):
        # Campo de velocidades de un remolino y una partícula que lo sigue
        def campo(p):
            x, y = p[0], p[1]
            return np.array([-y - 0.2 * x, x - 0.2 * y, 0]) * 0.5

        flechas = ArrowVectorField(campo, x_range=[-7, 7, 1],
                                   y_range=[-4, 4, 1])
        trayectoria = ParametricFunction(
            lambda t: 3.6 * np.exp(-0.2 * t)
            * np.array([np.cos(t), np.sin(t), 0]),
            t_range=[0, 12], color=YELLOW, stroke_width=5)
        particula = Dot(trayectoria.get_end(), color=YELLOW, radius=0.12)
        self.add(flechas, trayectoria, particula)
