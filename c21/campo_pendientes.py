from manim import *


def f(t, y):
    return t - y              # la EDO: y' = t - y


class CampoPendientes(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 4.5, 1], y_range=[-2.5, 4, 1],
                    x_length=10, y_length=6.2, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 24})
        rotulos = ejes.get_axis_labels(MathTex("t"), MathTex("y"))
        campo = VGroup()
        for t in np.arange(0.25, 4.5, 0.3):
            for y in np.arange(-2.25, 4, 0.3):
                m = f(t, y)
                # Dirección (1, m) llevada a la pantalla: respeta
                # las escalas distintas de los dos ejes
                v = ejes.c2p(t + 0.01, y + 0.01*m) - ejes.c2p(t, y)
                v = 0.14 * v / np.linalg.norm(v)
                centro = ejes.c2p(t, y)
                tono = interpolate_color(BLUE_D, YELLOW, abs(m) / 5)
                campo.add(Line(centro - v, centro + v, color=tono,
                               stroke_width=2))
        self.add(ejes, rotulos)
        self.play(Create(campo, lag_ratio=0.01), run_time=2)
        # Soluciones exactas y = t - 1 + C e^{-t}
        colores = color_gradient([TEAL, WHITE, RED], 6)
        soluciones = VGroup(*[
            ejes.plot(lambda t, C=C: t - 1 + C * np.exp(-t),
                      x_range=[0, 4.5], color=col, stroke_width=4)
            for C, col in zip([-1, 0, 1, 2, 3, 4], colores)])
        self.play(LaggedStart(*[Create(s) for s in soluciones],
                              lag_ratio=0.3), run_time=3)
        etiqueta = MathTex(r"y' = t - y", font_size=40)
        etiqueta.add_background_rectangle(opacity=0.8)
        self.play(Write(etiqueta.to_corner(UR)))
