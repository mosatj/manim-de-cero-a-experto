from manim import *
from metodos_edo import rk4, resolver


def lorenz(t, P, sigma=10.0, rho=28.0, beta=8 / 3):
    # P puede ser un estado (3,) o una nube de N estados (N, 3)
    x, y, z = P[..., 0], P[..., 1], P[..., 2]
    return np.stack([sigma * (y - x), x * (rho - z) - y,
                     x * y - beta * z], axis=-1)


class SensibilidadLorenz(Scene):
    def construct(self):
        N, h = 300, 0.005
        # Un estado sobre el atractor (tras 20 unidades de tiempo)
        _, base = resolver(rk4, lorenz, 0, np.ones(3), h, 4000)
        _, fondo_datos = resolver(rk4, lorenz, 0, base[-1], h, 8000)
        # 300 vecinos repartidos en un segmento de longitud 1e-5
        P0 = np.tile(base[-1], (N, 1))
        P0[:, 0] += np.linspace(0, 1e-5, N)
        # Toda la nube a la vez: forma (4001, 300, 3), t de 0 a 20
        _, nube = resolver(rk4, lorenz, 0, P0, h, 4000)
        ejes = Axes(x_range=[-22, 22, 10], y_range=[0, 50, 10],
                    x_length=7, y_length=7.4, tips=False)
        fondo = VMobject(stroke_width=1, stroke_opacity=0.3)
        fondo.set_points_smoothly(
            [ejes.c2p(q[0], q[2]) for q in fondo_datos[::3]])
        # El color identifica la condición inicial de cada punto
        colores = color_gradient([BLUE, TEAL, YELLOW, RED], N)
        t = ValueTracker(0)
        puntos = always_redraw(lambda: VGroup(*[
            Dot(ejes.c2p(q[0], q[2]), radius=0.08, color=c) for q, c
            in zip(nube[round(t.get_value() / h)], colores)]))
        reloj = always_redraw(lambda: MathTex(
            f"t = {t.get_value():.0f}", font_size=60).to_corner(UL))
        self.add(fondo, puntos, reloj)
        for tiempo in (10, 14, 17, 20):
            self.play(t.animate.set_value(tiempo), run_time=3,
                      rate_func=linear)
