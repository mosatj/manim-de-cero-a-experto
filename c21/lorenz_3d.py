from manim import *
from metodos_edo import rk4, resolver


def lorenz(t, p, sigma=10.0, rho=28.0, beta=8 / 3):
    x, y, z = p[..., 0], p[..., 1], p[..., 2]     # (3,) o (N, 3)
    return np.stack([sigma * (y - x), x * (rho - z) - y,
                     x * y - beta * z], axis=-1)


class Lorenz3D(ThreeDScene):
    def construct(self):
        ejes = ThreeDAxes(
            x_range=[-25, 25, 10], y_range=[-30, 30, 10],
            z_range=[0, 50, 10], x_length=6, y_length=7, z_length=6,
            tips=False).shift(3 * IN)
        self.set_camera_orientation(phi=70 * DEGREES,
                                    theta=-45 * DEGREES, zoom=1.0)
        # 1) Datos: se calculan una sola vez, fuera de la animación
        _, datos = resolver(rk4, lorenz, 0, np.ones(3), 5e-3, 8000)
        puntos = ejes.c2p(datos)                # forma (8001, 3)
        # 2) Curva en 40 tramos con color progresivo (azul -> rojo)
        tramos = VGroup()
        cortes = np.linspace(0, len(puntos) - 1, 41).astype(int)
        colores = color_gradient([BLUE, TEAL, YELLOW, RED], 40)
        for k in range(40):
            tramo = VMobject(stroke_width=1.5, color=colores[k])
            a, b = cortes[k], cortes[k + 1] + 1
            tramo.set_points_smoothly(puntos[a:b])
            tramos.add(tramo)
        self.add(ejes)
        self.play(Succession(*[Create(t, rate_func=linear)
                               for t in tramos]), run_time=8)
        self.move_camera(theta=20 * DEGREES, run_time=3)
