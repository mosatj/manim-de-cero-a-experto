from manim import *


class CubicaSinExtremo(Scene):
    def construct(self):
        ejes = Axes(x_range=[-1.6, 1.6, 0.5], y_range=[-3, 3, 1],
                    x_length=7, y_length=6, tips=False)
        ejes.add_coordinates(font_size=20)
        curva = ejes.plot(lambda x: x**3, x_range=[-1.44, 1.44],
                          color=BLUE)
        horizontal = Line(ejes.c2p(-1, 0), ejes.c2p(1, 0),
                          color=YELLOW,
                          stroke_width=6)
        punto = Dot(ejes.c2p(0, 0), color=YELLOW)
        nota = MathTex(r"f'(0)=0", r"\text{ pero } f(x)<0<f(y)",
                       r"\text{ si } x<0<y", font_size=36)
        nota.to_edge(UP).set_color_by_tex("f'(0)", YELLOW)
        self.add(ejes, curva, horizontal, punto, nota)
