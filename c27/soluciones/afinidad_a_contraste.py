from manim import *

f = lambda x: 0.2 * x**3 - 1.2 * x + 3
A, B, C = -1.5, 3, 1.5


class AfinidadAContraste(Scene):
    def construct(self):
        ejes = Axes(x_range=[-2.5, 3.5], y_range=[0, 5.5], x_length=7,
                    y_length=5.4, tips=False).to_edge(LEFT, buff=0.6)
        curva = ejes.plot(f, x_range=[-2.4, 3.15])
        secante = Line(ejes.c2p(A, f(A)), ejes.c2p(B, f(B)))
        m = (f(B) - f(A)) / (B - A)
        tangente = ejes.plot(lambda x: f(C) + m * (x - C),
                             x_range=[C - 1.7, C + 1.7])
        punto_c = Dot(ejes.c2p(C, f(C)))
        formula = MathTex(r"f'(c)", "=", r"\frac{f(b)-f(a)}{b-a}",
                          font_size=40).to_edge(RIGHT, buff=1)
        VGroup(ejes, curva, secante, tangente, punto_c,
               formula).set_color(WHITE)
        for linea in (ejes, curva, secante, tangente):
            linea.set_stroke(width=3)
        # 1. Presentación afín: todo en el mismo registro
        self.play(Create(ejes), Create(curva))
        self.play(Create(secante), Create(tangente), FadeIn(punto_c))
        self.play(Write(formula))
        self.wait()
        # 2. La idea: un solo gesto atenúa el contexto y enciende el foco
        destino = formula.copy().scale(1.5).to_edge(RIGHT, buff=0.5)
        destino[0].set_color(ORANGE)
        destino[2].set_color(GRAY)
        self.play(
            ejes.animate.set_stroke(GRAY, 2, opacity=0.5),
            secante.animate.set_color(GRAY),
            curva.animate.set_stroke(BLUE, 4),
            tangente.animate.set_stroke(ORANGE, 9),
            punto_c.animate.set_color(ORANGE).scale(1.8),
            Transform(formula, destino),
            run_time=1.5,
        )
        self.wait(2)
