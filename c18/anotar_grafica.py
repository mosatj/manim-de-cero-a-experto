from manim import *


class AnotarGrafica(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 6, 1], y_range=[0, 5, 1],
                    x_length=8, y_length=5.5, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 26})
        curva = ejes.plot(lambda x: 0.12 * x ** 2 + 0.5, color=BLUE)
        # 1. Un punto de la gráfica y sus proyecciones
        p = ejes.input_to_graph_point(4, curva)       # o ejes.i2gp
        punto = Dot(p, color=YELLOW)
        proyecciones = ejes.get_lines_to_point(p, color=YELLOW)
        et_punto = MathTex(r"(4,\,f(4))", font_size=34)
        et_punto.set_color(YELLOW)
        et_punto.next_to(punto, UL, buff=0.1)
        # 2. Una marca en T sobre el eje x, con su rótulo
        marca_t = ejes.get_T_label(x_val=2, graph=curva, label="a",
                                   line_color=RED,
                                   triangle_color=RED)
        # 3. El nombre de la curva, pegado a ella
        nombre = ejes.get_graph_label(curva, "f", x_val=5.5,
                                      direction=UL)
        self.add(ejes, curva, nombre)
        self.play(Create(proyecciones), FadeIn(punto, et_punto))
        self.play(FadeIn(marca_t))
        self.wait()
