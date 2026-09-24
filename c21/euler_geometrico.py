from manim import *

f = lambda t, y: y - t**2 + 1
exacta = lambda t: (t + 1)**2 - 0.5 * np.exp(t)


class EulerGeometrico(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 2.2, 0.5], y_range=[0, 6, 1],
                    x_length=9, y_length=6, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 24}).shift(LEFT * 1.5)
        curva = ejes.plot(exacta, x_range=[0, 2], color=BLUE)
        leyenda = VGroup(
            MathTex(r"y' = y - t^2 + 1,\ y(0) = 0.5", font_size=32),
            MathTex(r"y_{i+1} = y_i + h\,f(t_i, y_i)", font_size=32,
                    color=YELLOW),
            MathTex(r"h = 0.5", font_size=32, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UR)
        self.add(ejes, curva, leyenda)
        h, t, y = 0.5, 0.0, 0.5
        punto = Dot(ejes.c2p(t, y), color=YELLOW)
        self.add(punto)
        for _ in range(4):
            t1, y1 = t + h, y + h * f(t, y)       # un paso de Euler
            tangente = Line(ejes.c2p(t, y), ejes.c2p(t1, y1),
                            color=YELLOW, stroke_width=5)
            nuevo = Dot(ejes.c2p(t1, y1), color=YELLOW)
            error = DashedLine(ejes.c2p(t1, y1),
                               ejes.c2p(t1, exacta(t1)), color=RED)
            self.play(Create(tangente), FadeIn(nuevo),
                      Create(error), run_time=1.2)
            t, y = t1, y1
        texto = MathTex(r"y_4 = 4.4375", r"\quad y(2) \approx 5.31",
                        font_size=32).next_to(leyenda, DOWN,
                                              aligned_edge=LEFT)
        texto[1].set_color(BLUE)
        self.add(texto)
