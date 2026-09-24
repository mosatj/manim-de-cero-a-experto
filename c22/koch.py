from manim import *


class CurvaKoch(VMobject):
    """Curva de Koch de nivel n entre dos puntos."""

    def __init__(self, inicio, fin, nivel=0, **kwargs):
        super().__init__(**kwargs)
        self.nivel = nivel
        extremos = [np.array(inicio, float), np.array(fin, float)]
        vertices = self.subdividir(extremos, nivel)
        self.set_points_as_corners(vertices)

    @staticmethod
    def subdividir(puntos, nivel):
        for _ in range(nivel):
            nuevos = [puntos[0]]
            for p, q in zip(puntos[:-1], puntos[1:]):
                d = (q - p) / 3
                pico = p + d + rotate_vector(d, PI / 3)  # a la izq.
                nuevos += [p + d, pico, p + 2 * d, q]
            puntos = nuevos
        return puntos


class CopoKoch(Scene):
    def construct(self):
        # Triángulo equilátero recorrido en sentido horario
        angulos = PI / 2 - TAU / 3 * np.arange(3)
        v = [3.2 * np.array([np.cos(a), np.sin(a), 0]) - 0.5 * UP
             for a in angulos]
        copo = lambda n: VGroup(*[
            CurvaKoch(v[i], v[(i + 1) % 3], n, color=BLUE,
                      stroke_width=3)
            for i in range(3)])
        actual = copo(0)
        self.add(actual)
        for n in (1, 2, 3, 4):
            self.play(Transform(actual, copo(n)), run_time=1.5)
        self.add(MathTex(r"P_n = 3\ell\left(\tfrac43\right)^{n}",
                         font_size=40).to_corner(UL))
