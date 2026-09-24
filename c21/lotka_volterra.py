from manim import *
from metodos_edo import rk4, resolver

A, B, G, D = 2 / 3, 4 / 3, 1.0, 1.0      # alfa, beta, gamma, delta


def F(t, p):
    x, y = p                              # presas, depredadores
    return np.array([A * x - B * x * y, D * x * y - G * y])


class LotkaVolterra(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 3.2, 1], y_range=[0, 2, 0.5],
                    x_length=9, y_length=6.2, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 24})
        rot = ejes.get_axis_labels(
            Tex("presas $x$", font_size=32),
            Tex("depredadores $y$", font_size=32))

        def en_pantalla(p):
            # El campo vive en coordenadas de los ejes: se traduce
            x, y = ejes.p2c(p)[:2]
            u = F(0, (x, y))
            return ejes.c2p(x + u[0], y + u[1]) - ejes.c2p(x, y)

        esq1, esq2 = ejes.c2p(0.15, 0.1), ejes.c2p(3.15, 2)
        campo = ArrowVectorField(
            en_pantalla, x_range=[esq1[0], esq2[0], 0.6],
            y_range=[esq1[1], esq2[1], 0.6],
            length_func=lambda n: 0.4 * np.tanh(n), opacity=0.5)
        self.add(ejes, rot, campo)
        colores = color_gradient([TEAL, YELLOW, RED], 4)
        for y0, color in zip((0.9, 1.2, 1.5, 1.8), colores):
            # El mismo RK4 de metodos_edo.py, ahora con un vector
            _, datos = resolver(rk4, F, 0, np.array([1.0, y0]),
                                0.01, 1300)
            orbita = VMobject(color=color, stroke_width=4)
            orbita.set_points_smoothly(ejes.c2p(datos))
            self.play(Create(orbita), run_time=1)
        self.add(Dot(ejes.c2p(G / D, A / B), color=WHITE))
