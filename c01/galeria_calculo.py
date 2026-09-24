from manim import *


class GaleriaCalculo(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 4, 1], y_range=[0, 5, 1],
                    x_length=9, y_length=5.5, tips=False)
        curva = ejes.plot(lambda x: 0.3 * x**2 + 0.5, color=BLUE)
        rect = ejes.get_riemann_rectangles(curva, x_range=[0.5, 3.5],
                                           dx=0.25, fill_opacity=0.6)
        x0 = 2.5
        pendiente = 0.6 * x0
        tangente = ejes.plot(
            lambda x: 0.3 * x0**2 + 0.5 + pendiente * (x - x0),
            x_range=[1.2, 3.9], color=YELLOW)
        punto = Dot(ejes.c2p(x0, 0.3 * x0**2 + 0.5), color=YELLOW)
        formula = MathTex(r"\int_{0.5}^{3.5} f(x)\,dx", font_size=48)
        formula.move_to(ejes.c2p(1.2, 4))
        self.add(ejes, rect, curva, tangente, punto, formula)
