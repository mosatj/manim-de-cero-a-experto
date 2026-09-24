from manim import *


class MontecarloArea(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 1, 0.5], y_range=[0, 1, 0.5],
                    x_length=6, y_length=6, tips=False,
                    axis_config={"include_numbers": True})
        ejes.to_edge(LEFT)
        curva = ejes.plot(lambda x: x ** 2, color=YELLOW)
        rng = np.random.default_rng(1)
        p = rng.uniform(0, 1, size=(1500, 2))
        debajo = p[:, 1] <= p[:, 0] ** 2
        nube = VGroup(*[Dot(ejes.c2p(x, y), radius=0.025,
                            color=TEAL_C if d else GREY_D)
                        for (x, y), d in zip(p, debajo)])
        texto = MathTex(r"\int_0^1 x^2\,dx \approx",
                        f"{debajo.mean():.3f}",
                        font_size=44)
        exacto = MathTex(r"\text{exacto: } \tfrac13 \approx 0.333",
                         font_size=40)
        VGroup(texto, exacto).arrange(DOWN, buff=0.5).to_edge(RIGHT)
        self.add(ejes, curva)
        self.play(LaggedStart(*[FadeIn(d) for d in nube],
                              lag_ratio=0.002),
                  run_time=3)
        self.play(Write(texto), Write(exacto))
        self.wait()
