from manim import *


def grafica(f, x_range, y_range, nombre, color=BLUE, ancho=5.5,
            alto=3.5):
    """Ejes sobrios, curva y rótulo directo: el estilo del libro."""
    ejes = Axes(x_range=x_range, y_range=y_range, x_length=ancho,
                y_length=alto, tips=False,
                axis_config={"color": GRAY_B, "stroke_width": 1.5,
                             "include_numbers": True,
                             "font_size": 22})
    curva = ejes.plot(f, x_range=x_range[:2], color=color,
                      stroke_width=3)
    rotulo = MathTex(nombre, color=color, font_size=34)
    rotulo.next_to(curva.get_end(), UP, buff=0.15)
    return VGroup(ejes, curva, rotulo)


class ComponenteGrafica(Scene):
    def construct(self):
        izq = grafica(lambda x: np.exp(-x) * np.cos(3 * x),
                      [0, 6, 1], [-1, 1, 0.5], r"e^{-x}\cos 3x")
        der = grafica(lambda x: x / (1 + x ** 2), [-5, 5, 1],
                      [-0.6, 0.6, 0.2], r"\frac{x}{1+x^2}",
                      color=YELLOW)
        VGroup(izq, der).arrange(RIGHT, buff=0.8)
        self.add(izq, der)
