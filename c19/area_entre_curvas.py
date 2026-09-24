from manim import *


class AreaEntreCurvas(Scene):
    def construct(self):
        f = lambda x: 4 - x**2               # curva de arriba
        g = lambda x: x + 2                  # curva de abajo
        ejes = Axes(x_range=[-3, 2, 1], y_range=[-1, 5, 1],
                    x_length=6.5, y_length=6.5, tips=False)
        ejes.add_coordinates(font_size=22).to_edge(LEFT, buff=0.5)
        graf_f = ejes.plot(f, x_range=[-2.6, 1.6], color=BLUE)
        graf_g = ejes.plot(g, x_range=[-2.6, 1.6], color=GREEN)
        nom_f = MathTex(r"y=4-x^2", color=BLUE).scale(0.7)
        nom_g = MathTex(r"y=x+2", color=GREEN).scale(0.7)
        nom_f.next_to(ejes.c2p(0, 4), UR, buff=0.1)
        nom_g.next_to(ejes.c2p(1.6, 3.6), RIGHT, buff=0.1)
        # Cortes: 4 - x² = x + 2  <=>  (x + 2)(x - 1) = 0
        area = ejes.get_area(graf_f, [-2, 1], bounded_graph=graf_g,
                             color=YELLOW, opacity=0.35)
        cortes = VGroup(*[Dot(ejes.c2p(v, g(v))) for v in (-2, 1)])

        # Rectángulo representativo de ancho Δx y alto f(x) − g(x)
        x = ValueTracker(-1.7)
        dx = 0.18
        tira = always_redraw(lambda: Polygon(
            ejes.c2p(x.get_value(), g(x.get_value())),
            ejes.c2p(x.get_value() + dx, g(x.get_value())),
            ejes.c2p(x.get_value() + dx, f(x.get_value())),
            ejes.c2p(x.get_value(), f(x.get_value())),
            color=RED, fill_opacity=0.8, stroke_width=1))
        llave = always_redraw(lambda: BraceBetweenPoints(
            ejes.c2p(x.get_value(), f(x.get_value())),
            ejes.c2p(x.get_value(), g(x.get_value())), LEFT))

        formula = MathTex(
            r"A&=\int_{-2}^{1}\big[f(x)-g(x)\big]\,dx\\",
            r"&=\int_{-2}^{1}\left(2-x-x^2\right)dx\\",
            r"&=\Big[2x-\tfrac{x^2}{2}-\tfrac{x^3}{3}\Big]_{-2}^{1}"
            r"=\frac{9}{2}", font_size=38)
        formula.to_edge(RIGHT, buff=0.4)

        self.play(Create(ejes), Create(graf_f), Create(graf_g),
                  Write(nom_f), Write(nom_g))
        self.play(FadeIn(cortes), FadeIn(area))
        self.play(FadeIn(tira), GrowFromCenter(llave),
                  Write(formula[0]))
        self.play(x.animate.set_value(0.6), run_time=3)
        self.play(Write(formula[1]))
        self.play(Write(formula[2]))
