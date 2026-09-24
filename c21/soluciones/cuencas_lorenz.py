from manim import *


def lorenz(P, sigma=10.0, rho=28.0, beta=8 / 3):
    x, y, z = P[:, 0], P[:, 1], P[:, 2]
    return np.column_stack([sigma * (y - x), x * (rho - z) - y,
                            x * y - beta * z])


class CuencasLorenz(Scene):
    def construct(self):
        n, h, pasos = 70, 0.005, 1000          # 4900 estados, t = 5
        xs = np.linspace(-1, 1, n)
        X, Y = np.meshgrid(xs, xs)
        P = np.column_stack([X.ravel(), Y.ravel(),
                             np.full(n * n, 25.0)])
        for _ in range(pasos):         # RK4 sobre la nube entera
            k1 = lorenz(P)
            k2 = lorenz(P + h / 2 * k1)
            k3 = lorenz(P + h / 2 * k2)
            k4 = lorenz(P + h * k3)
            P = P + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        ejes = Axes(x_range=[-1, 1, 0.5], y_range=[-1, 1, 0.5],
                    x_length=6.6, y_length=6.6, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 20})
        lado = 6.6 / n
        celdas = VGroup()
        for (x0, y0), xf in zip(zip(X.ravel(), Y.ravel()), P[:, 0]):
            celda = Square(lado, stroke_width=0, fill_opacity=1)
            celda.set_fill(BLUE if xf < 0 else ORANGE)
            celdas.add(celda.move_to(ejes.c2p(x0, y0)))
        leyenda = VGroup(
            Tex(r"$x(5) < 0$", color=BLUE),
            Tex(r"$x(5) > 0$", color=ORANGE),
            MathTex(r"z_0 = 25", font_size=40),
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT, buff=1)
        self.add(celdas, ejes)
        self.play(FadeIn(leyenda))
