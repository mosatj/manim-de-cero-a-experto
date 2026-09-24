from manim import *


class ContraejemploAbs(Scene):
    """«Toda función continua es derivable» es falso: f(x) = |x|."""

    def construct(self):
        ejes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 3, 1],
            x_length=7,
            y_length=4.5,
        ).shift(DOWN * 0.3)
        grafica = ejes.plot(
            lambda x: abs(x), color=BLUE, use_smoothing=False
        )
        titulo = MathTex(
            r"f(x)=|x|", r"\text{ es continua en } 0", font_size=40
        ).to_edge(UP)
        self.play(Create(ejes), Create(grafica), Write(titulo))

        h = ValueTracker(2.5)
        origen = ejes.c2p(0, 0)

        def secante(signo, color):
            return always_redraw(
                lambda: Line(
                    origen,
                    ejes.c2p(signo * h.get_value(), h.get_value()),
                    color=color,
                ).scale(
                    3.5 / max(h.get_value(), 0.05),
                    about_point=origen,
                )
            )

        derecha, izquierda = secante(1, GREEN), secante(-1, RED)
        self.play(Create(derecha), Create(izquierda))
        self.play(h.animate.set_value(0.4), run_time=3)
        pendientes = (
            VGroup(
                MathTex(
                    r"\lim_{h\to 0^+}\frac{|h|}{h} = 1", color=GREEN
                ),
                MathTex(
                    r"\lim_{h\to 0^-}\frac{|h|}{h} = -1", color=RED
                ),
            )
            .scale(0.8)
            .arrange(DOWN, aligned_edge=LEFT)
            .to_corner(DR)
        )
        self.play(Write(pendientes))
        nuevo = MathTex(
            r"f(x)=|x|",
            r"\text{ no es derivable en } 0",
            font_size=40,
        ).to_edge(UP)
        self.play(TransformMatchingTex(titulo, nuevo))
