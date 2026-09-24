from manim import *


class EscalaLog(Scene):
    def construct(self):
        # En un eje logarítmico, y_range da EXPONENTES: 10^0 a 10^6
        ejes = Axes(
            x_range=[0, 10, 1], y_range=[0, 6, 1],
            x_length=9, y_length=6, tips=False,
            x_axis_config={"font_size": 26},
            y_axis_config={"scaling": LogBase(base=10)},
        )
        ejes.add_coordinates()     # en el eje y, rótulos 10^k
        exponencial = ejes.plot(lambda x: 4 ** x, x_range=[0, 9.9],
                                color=YELLOW)
        potencia = ejes.plot(lambda x: x ** 3, x_range=[1, 10],
                             color=BLUE)
        et_exp = ejes.get_graph_label(exponencial, "4^x", x_val=9,
                                      direction=UL)
        et_pot = ejes.get_graph_label(potencia, "x^3", x_val=10,
                                      direction=DOWN)
        self.add(ejes)
        self.play(Create(exponencial), Create(potencia), run_time=2)
        self.play(FadeIn(et_exp, et_pot))
        self.wait()
