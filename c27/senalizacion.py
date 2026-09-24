from manim import *


def pendiente(color_dx=WHITE, color_dy=WHITE):
    ejes = Axes(x_range=[0, 4], y_range=[0, 9], x_length=5, y_length=5)
    curva = ejes.plot(lambda x: 0.5 * x**2 + 1.5, color=BLUE)
    p, q, esquina = ejes.c2p(1, 2), ejes.c2p(3, 6), ejes.c2p(3, 2)
    secante = Line(p, q, color=GREY_B)
    dx = Line(p, esquina, color=color_dx)
    dy = Line(esquina, q, color=color_dy)
    return VGroup(ejes, curva, secante, dx, dy).to_edge(LEFT)


class SenalizacionAntes(Scene):
    def construct(self):
        figura = pendiente()
        formula = MathTex(r"m=\frac{\Delta y}{\Delta x}=\frac{4}{2}=2",
                          font_size=60)
        formula.to_edge(RIGHT, buff=1.2)
        self.play(Create(figura), Write(formula))


class SenalizacionDespues(Scene):
    def construct(self):
        figura = pendiente(color_dx=TEAL, color_dy=ORANGE)
        dx, dy = figura[3], figura[4]
        rotulo_dx = MathTex(r"\Delta x", color=TEAL).next_to(dx, DOWN)
        rotulo_dy = MathTex(r"\Delta y", color=ORANGE)
        rotulo_dy.next_to(dy, RIGHT)
        formula = MathTex(r"m=\frac{\Delta y}{\Delta x}=\frac{4}{2}=2",
                          font_size=60)
        glifos = formula[0]  # m = Δ y — Δ x = 4 — 2 = 2
        for k in (2, 3, 8):  # Δy y su valor, en naranja
            glifos[k].set_color(ORANGE)
        for k in (5, 6, 10):  # Δx y su valor, en verde azulado
            glifos[k].set_color(TEAL)
        formula.to_edge(RIGHT, buff=1.2)
        self.play(Create(figura))
        self.play(Write(rotulo_dx), Write(rotulo_dy))
        self.play(Write(formula))
        self.play(Circumscribe(formula[-1], color=YELLOW))
