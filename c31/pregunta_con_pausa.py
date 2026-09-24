from manim import *


class PausaYPredice(Scene):
    def construct(self):
        # 1. La situación: un cuadrado de lado 1
        cuadrado = Square(1.2, color=BLUE, fill_opacity=0.5).shift(
            LEFT * 4
        )
        pregunta = Text(
            "Si duplicas el lado, ¿cuántas veces crece el área?",
            font_size=32,
        ).to_edge(UP)
        self.play(DrawBorderThenFill(cuadrado), Write(pregunta))

        # 2. Invitación explícita a pausar y predecir
        barras = VGroup(
            Rectangle(height=0.8, width=0.22),
            Rectangle(height=0.8, width=0.22),
        ).arrange(RIGHT, buff=0.22)
        barras.set_fill(YELLOW, 1).set_stroke(width=0)
        anillo = Circle(0.75, color=YELLOW)
        pausa = VGroup(anillo, barras)
        aviso = Text("Pausa y predice", font_size=28, color=YELLOW)
        aviso.next_to(pausa, DOWN)
        self.play(FadeIn(pausa, scale=0.5), FadeIn(aviso))
        self.play(Uncreate(anillo), run_time=4, rate_func=linear)
        self.play(FadeOut(barras), FadeOut(aviso))

        # 3. La respuesta, construida y no solo dicha
        grande = VGroup(*[cuadrado.copy() for _ in range(4)])
        grande.arrange_in_grid(2, 2, buff=0).move_to(RIGHT * 3)
        self.play(
            LaggedStart(
                *[TransformFromCopy(cuadrado, c) for c in grande],
                lag_ratio=0.3,
            )
        )
        respuesta = MathTex(r"(2\ell)^2 = 4\,\ell^2", font_size=56)
        respuesta.next_to(grande, DOWN, buff=0.5)
        self.play(Write(respuesta))
