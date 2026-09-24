from manim import *


class TeoremaConRitmo(Scene):
    def construct(self):
        titulo = Text("Teorema de Pitágoras", font_size=44)
        titulo.to_edge(UP)
        triangulo = Polygon([-2, -1.5, 0], [2, -1.5, 0],
                            [2, 1.5, 0], color=BLUE,
                            fill_opacity=0.3)
        triangulo.shift(3 * LEFT)
        a = MathTex("a").next_to(triangulo, RIGHT)
        b = MathTex("b").next_to(triangulo, DOWN)
        c = MathTex("c").move_to(triangulo.get_center()
                                 + 0.8 * UL)
        formula = MathTex("a^2", "+", "b^2", "=", "c^2",
                          font_size=80).shift(3 * RIGHT)

        self.play(Write(titulo), run_time=1.5)
        self.wait(0.5)
        self.play(DrawBorderThenFill(triangulo), run_time=1.5)
        # Los tres nombres, en cascada: se leen uno a uno
        self.play(LaggedStart(
            *[FadeIn(m, scale=1.8) for m in (a, b, c)],
            lag_ratio=0.4))
        self.play(FadeIn(formula, shift=UP), run_time=1.5)
        self.wait(2)   # tiempo para leer la fórmula final
