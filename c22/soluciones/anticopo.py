from manim import *


def koch(p, q, nivel, signo=1):
    """Vértices de Koch; con signo=-1 el pico va hacia dentro."""
    puntos = [p, q]
    for _ in range(nivel):
        nuevos = [puntos[0]]
        for a, b in zip(puntos[:-1], puntos[1:]):
            d = (b - a) / 3
            pico = a + d + rotate_vector(d, signo * PI / 3)
            nuevos += [a + d, pico, a + 2 * d, b]
        puntos = nuevos
    return puntos


class Anticopo(Scene):
    def construct(self):
        ang = PI / 2 - TAU / 3 * np.arange(3)
        v = [3.4 * np.array([np.cos(a), np.sin(a), 0]) for a in ang]
        grupo = VGroup()
        for i in range(3):
            lado = VMobject(color=BLUE)
            vert = koch(v[i], v[(i + 1) % 3], 4, signo=-1)
            lado.set_points_as_corners(vert)
            grupo.add(lado)
        self.play(Create(grupo), run_time=3)
