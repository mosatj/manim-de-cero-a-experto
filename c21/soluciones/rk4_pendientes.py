from manim import *

f = lambda t, y: y - t**2 + 1
exacta = lambda t: (t + 1)**2 - 0.5 * np.exp(t)


class RK4Pendientes(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 1.1, 0.5], y_range=[0, 3, 1],
                    x_length=7, y_length=6, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 24}).to_edge(LEFT)
        P = ejes.c2p
        h, t0, y0 = 1.0, 0.0, 0.5
        p1 = f(t0, y0)
        p2 = f(t0 + h / 2, y0 + h / 2 * p1)
        p3 = f(t0 + h / 2, y0 + h / 2 * p2)
        p4 = f(t0 + h, y0 + h * p3)
        y1 = y0 + h / 6 * (p1 + 2 * p2 + 2 * p3 + p4)
        curva = ejes.plot(exacta, x_range=[0, 1.05], color=BLUE)
        self.add(ejes, curva)
        # Cada pendiente, como un segmento corto en su punto
        muestras = ((t0, y0, p1, GREEN),
                    (0.5, y0 + 0.5 * p1, p2, TEAL),
                    (0.5, y0 + 0.5 * p2, p3, PURPLE),
                    (1.0, y0 + p3, p4, ORANGE))
        for t, y, m, color in muestras:
            v = 0.15 * np.array([1, m])
            self.play(Create(Line(P(t - v[0], y - v[1]),
                                  P(t + v[0], y + v[1]),
                                  color=color, stroke_width=6)),
                      FadeIn(Dot(P(t, y), color=color)))
        self.play(Create(Line(P(t0, y0), P(1, y1), color=WHITE)))
        self.add(Dot(P(1, y1), color=WHITE),
                 MathTex(rf"y_1 = {y1:.4f}", r"\quad y(1) = 2.6409",
                         font_size=36).to_edge(RIGHT))
