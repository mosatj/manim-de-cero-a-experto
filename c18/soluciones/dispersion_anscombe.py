from manim import *

# Primer conjunto del cuarteto de Anscombe (1973)
X = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
Y = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82,
     5.68]


class DispersionAnscombe(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 16, 2], y_range=[0, 12, 2],
                    x_length=9, y_length=6, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 24})
        puntos = VGroup(*[Dot(ejes.c2p(x, y), color=YELLOW)
                          for x, y in zip(X, Y)])
        # Recta de mínimos cuadrados calculada con NumPy
        m, b = np.polyfit(X, Y, 1)
        recta = ejes.plot(lambda x: m * x + b, x_range=[2, 16],
                          color=BLUE)
        ecuacion = MathTex(rf"y={b:.2f}+{m:.3f}\,x", color=BLUE)
        ecuacion.next_to(ejes.c2p(16, m * 16 + b), UL)
        self.add(ejes, recta, puntos, ecuacion)
