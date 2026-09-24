from manim import *


class AreaRaizParabola(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 1.2, 0.5], y_range=[0, 1.2, 0.5],
                    x_length=6, y_length=6, tips=False)
        ejes.add_coordinates(font_size=22).to_edge(LEFT)
        # Paso fino: √x tiene tangente vertical en 0
        arriba = ejes.plot(np.sqrt, x_range=[0, 1.2, 0.002],
                           color=BLUE)
        abajo = ejes.plot(lambda x: x**2, x_range=[0, 1.09],
                          color=GREEN)
        area = ejes.get_area(arriba, [0, 1], bounded_graph=abajo,
                             color=YELLOW, opacity=0.4)
        cuenta = MathTex(
            r"A=\int_0^1\left(\sqrt{x}-x^2\right)dx",
            r"=\Big[\tfrac{2}{3}x^{3/2}-\tfrac{x^3}{3}\Big]_0^1",
            r"=\frac{1}{3}", font_size=38)
        cuenta.arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT)
        self.add(ejes, area, arriba, abajo, cuenta)
