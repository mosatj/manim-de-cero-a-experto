from manim import *


def campo(p):
    theta, omega = p[0], p[1]
    return np.array([omega, -np.sin(theta) - 0.3 * omega, 0])


class PenduloAmortiguado(Scene):
    def construct(self):
        lineas = StreamLines(campo, x_range=[-7, 7, 0.5],
                             y_range=[-4, 4, 0.5], stroke_width=1.5,
                             virtual_time=5, padding=0.2)
        # Una órbita con RK4 desde (theta, omega) = (-6.5, 3.5)
        p, h, puntos = np.array([-6.5, 3.5, 0.0]), 0.02, []
        for _ in range(1500):
            k1 = campo(p)
            k2 = campo(p + h / 2 * k1)
            k3 = campo(p + h / 2 * k2)
            k4 = campo(p + h * k3)
            p = p + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            puntos.append(p.copy())
        orbita = VMobject(color=WHITE, stroke_width=5)
        orbita.set_points_smoothly(puntos[::3])
        self.add(lineas)
        self.play(Create(orbita), run_time=4)
        self.add(Dot(puntos[-1], color=RED))
