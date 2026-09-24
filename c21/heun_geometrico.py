from manim import *

f = lambda t, y: y - t**2 + 1
exacta = lambda t: (t + 1)**2 - 0.5 * np.exp(t)


class HeunGeometrico(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 1.2, 0.5], y_range=[0, 3, 1],
                    x_length=7, y_length=6, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 24}).to_edge(LEFT)
        h, t0, y0 = 1.0, 0.0, 0.5            # paso grande: se ve
        k1 = f(t0, y0)                       # 1.5
        y_pred = y0 + h * k1                 # 2.0 (Euler)
        k2 = f(t0 + h, y_pred)               # 2.0
        y1 = y0 + h / 2 * (k1 + k2)          # 2.25
        P = lambda t, y: ejes.c2p(t, y)
        curva = ejes.plot(exacta, x_range=[0, 1.1], color=BLUE)
        pred = Line(P(0, y0), P(1, y_pred), color=GOLD)
        # la pendiente k2, dibujada desde el inicio (discontinua)
        pend2 = DashedLine(P(0, y0), P(1, y0 + k2), color=RED)
        corr = Line(P(0, y0), P(1, y1), color=GREEN, stroke_width=6)
        self.add(ejes, curva, Dot(P(0, y0)))
        self.play(Create(pred),
                  FadeIn(Dot(P(1, y_pred), color=GOLD)))
        self.play(Create(pend2))
        self.play(Create(corr), FadeIn(Dot(P(1, y1), color=GREEN)))
        self.add(Dot(P(1, exacta(1)), color=BLUE))
        textos = VGroup(
            MathTex(r"k_1 = f(t_0, y_0) = 1.5", color=GOLD),
            MathTex(r"y^{*}_1 = y_0 + h k_1 = 2", color=GOLD),
            MathTex(r"k_2 = f(t_1, y^{*}_1) = 2", color=RED),
            MathTex(r"y_1 = y_0 + \tfrac12 h\,(k_1 + k_2) = 2.25",
                    color=GREEN),
            MathTex(r"y(1) = 4 - e/2 \approx 2.641", color=BLUE),
        ).scale(0.75).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        self.add(textos.to_edge(RIGHT))
