from manim import *


class PendienteTangente(Scene):
    """Una lección corta partida en secciones con nombre."""

    def construct(self):
        self.next_section("curva")
        ejes = Axes(x_range=[0, 2.5, 1], y_range=[0, 6, 1],
                    x_length=6, y_length=6).to_edge(LEFT)
        curva = ejes.plot(lambda x: x**2, x_range=[0, 2.4],
                          color=BLUE_D)
        punto = Dot(ejes.c2p(1, 1), color=RED_D)
        self.play(Create(ejes), Create(curva), FadeIn(punto))

        self.next_section("secante")
        h = ValueTracker(1.2)  # la secante por x=1 y x=1+h
        secante = always_redraw(lambda: ejes.plot(
            lambda x: 1 + (2 + h.get_value()) * (x - 1),
            x_range=[0.2, 2.2], color=RED_D))
        self.play(Create(secante))

        self.next_section("limite")
        self.play(h.animate.set_value(0), run_time=3)

        self.next_section("resultado")
        formula = MathTex(r"f'(1) = \lim_{h\to 0}",
                          r"\frac{(1+h)^2-1}{h} = 2", font_size=48)
        self.play(Write(formula.to_edge(RIGHT)))
        self.wait()
