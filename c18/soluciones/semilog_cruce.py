from manim import *


class SemilogCruce(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 16, 2], y_range=[0, 7, 1],
                    x_length=10, y_length=6, tips=False,
                    x_axis_config={"font_size": 26},
                    y_axis_config={"scaling": LogBase()})
        ejes.add_coordinates()
        exp = ejes.plot(np.exp, x_range=[0, 16], color=YELLOW)
        pot = ejes.plot(lambda x: x ** 5, x_range=[1, 16],
                        color=BLUE)
        # Cortes de e^x = x^5 (calculados aparte): 1.30 y 12.71
        cortes = VGroup(*[Dot(ejes.c2p(x, x ** 5), color=RED)
                          for x in (1.2959, 12.7132)])
        et = VGroup(ejes.get_graph_label(exp, "e^x", x_val=15.5,
                                         direction=LEFT),
                    ejes.get_graph_label(pot, "x^5", x_val=15,
                                         direction=DR))
        self.add(ejes, exp, pot, cortes, et)
