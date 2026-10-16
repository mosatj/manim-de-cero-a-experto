from manim import *


def contenido(plano, color, grosor):
    """Parábola y = (x - 1)^2 - 3 con su vértice y sus dos ceros."""
    curva = plano.plot(lambda x: (x - 1) ** 2 - 3, x_range=[-1.6, 3.6],
                       color=color, stroke_width=grosor)
    puntos = [(1, -3), (1 - np.sqrt(3), 0), (1 + np.sqrt(3), 0)]
    rotulos = [r"(1,-3)", r"1-\sqrt{3}", r"1+\sqrt{3}"]
    lados = [RIGHT, UL, UR]
    marcas = VGroup()
    for (x, y), texto, lado in zip(puntos, rotulos, lados):
        punto = Dot(plano.c2p(x, y), radius=0.11)
        marcas.add(punto, MathTex(texto, font_size=40).next_to(punto,
                                                              lado))
    return VGroup(curva, marcas)


class CapasAntes(Scene):
    def construct(self):
        plano = NumberPlane(
            background_line_style={"stroke_color": BLUE,
                                   "stroke_width": 3},
            axis_config={"stroke_width": 6})
        self.play(Create(plano), Create(contenido(plano, BLUE, 3)))


class CapasDespues(Scene):
    def construct(self):
        plano = NumberPlane(
            background_line_style={"stroke_color": GRAY,
                                   "stroke_width": 1,
                                   "stroke_opacity": 0.5},
            axis_config={"stroke_color": GRAY_B, "stroke_width": 2})
        self.play(Create(plano), Create(contenido(plano, ORANGE, 8)))
