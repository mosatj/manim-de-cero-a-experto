from manim import *


class SumasParciales(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 40, 5], y_range=[0, 5, 1],
                    x_length=11, y_length=5.5, tips=False)
        ejes.add_coordinates(font_size=22).shift(0.3 * DOWN)
        armonica = np.cumsum([1 / k for k in range(1, 41)])
        basilea = np.cumsum([1 / k**2 for k in range(1, 41)])
        pts_h = VGroup(*[Dot(ejes.c2p(n, s), 0.05, color=RED)
                         for n, s in enumerate(armonica, start=1)])
        pts_b = VGroup(*[Dot(ejes.c2p(n, s), 0.05, color=BLUE)
                         for n, s in enumerate(basilea, start=1)])
        # Límite de la serie de Basilea (Euler, 1734): π²/6
        L = PI**2 / 6
        techo = DashedLine(ejes.c2p(0, L), ejes.c2p(40, L))
        nom_b = MathTex(
            r"\sum_{k=1}^{n}\frac{1}{k^2}\to\frac{\pi^2}{6}",
            color=BLUE, font_size=36)
        nom_b.next_to(ejes.c2p(40, L), UP).shift(LEFT)
        # H_n = ln n + γ + o(1): crece sin cota, pero muy despacio
        gamma = 0.5772156649
        log = ejes.plot(lambda x: np.log(x) + gamma,
                        x_range=[1, 40], color=GRAY)
        nom_h = MathTex(r"H_n=\sum_{k=1}^{n}\frac{1}{k}\to\infty",
                        color=RED, font_size=36)
        nom_h.next_to(ejes.c2p(40, armonica[-1]), UP).shift(LEFT)
        nom_log = MathTex(r"\ln n+\gamma", color=GRAY, font_size=32)
        nom_log.next_to(ejes.c2p(20, np.log(20) + gamma), DOWN)

        self.play(Create(ejes))
        self.play(LaggedStart(*[FadeIn(p) for p in pts_b],
                              lag_ratio=0.1), run_time=2)
        self.play(Create(techo), Write(nom_b))
        self.play(LaggedStart(*[FadeIn(p) for p in pts_h],
                              lag_ratio=0.1), run_time=2)
        self.play(Create(log), Write(nom_h), Write(nom_log))
