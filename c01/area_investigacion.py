from manim import *

config.frame_height = 4.6
config.pixel_height = round(config.pixel_width * 4.6 / config.frame_width)


def lorenz(inicio, pasos=5000, dt=0.006, s=10.0, r=28.0, b=8 / 3):
    """Integra el sistema de Lorenz con Runge-Kutta de orden 4."""
    def campo(p):
        x, y, z = p
        return np.array([s * (y - x), x * (r - z) - y, x * y - b * z])
    p = np.array(inicio, dtype=float)
    camino = [p]
    for _ in range(pasos):
        k1 = campo(p)
        k2 = campo(p + dt / 2 * k1)
        k3 = campo(p + dt / 2 * k2)
        k4 = campo(p + dt * k3)
        p = p + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        camino.append(p)
    return np.array(camino)


def trazo(camino, tono):
    # Proyección en el plano xz, centrada y escalada al marco
    puntos = np.column_stack([camino[:, 0] * 0.11,
                              (camino[:, 2] - 25) * 0.11,
                              np.zeros(len(camino))])
    return VMobject(stroke_color=tono, stroke_width=1.6).set_points_as_corners(
        puntos)


class AreaInvestigacion(Scene):
    def construct(self):
        a = lorenz([1.0, 1.0, 1.0])
        b = lorenz([1.0, 1.0, 1.0 + 1e-6])  # una millonésima de diferencia
        separacion = np.linalg.norm(a - b, axis=1)
        divergen = int(np.argmax(separacion > 1.0))
        atractor = VGroup(trazo(a[divergen:], BLUE),
                          trazo(b[divergen:], RED_C)).shift(LEFT * 3.2)
        # Separación de las dos trayectorias (escala logarítmica)
        ejes = Axes(x_range=[0, 30, 10], y_range=[-7, 2, 3], x_length=4.6,
                    y_length=3.4, tips=False,
                    axis_config={"include_numbers": False}).shift(RIGHT * 3.6)
        t = np.arange(len(a)) * 0.006
        curva = VMobject(stroke_color=GREY_B, stroke_width=3)
        curva.set_points_as_corners([ejes.c2p(ti, np.log10(si + 1e-12))
                                     for ti, si in zip(t[::10],
                                                       separacion[::10])])
        rotulo_x = Text("tiempo", font_size=24).next_to(ejes, DOWN, buff=0.1)
        rotulo_y = MathTex(r"\log_{10}\lVert a-b\rVert", font_size=30)
        rotulo_y.rotate(PI / 2).next_to(ejes, LEFT, buff=0.15)
        self.add(atractor, ejes, curva, rotulo_x, rotulo_y)
