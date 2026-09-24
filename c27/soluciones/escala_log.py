from manim import *


class EscalaLog(Scene):
    def construct(self):
        # En escala logarítmica, 10^x es una recta
        ejes = Axes(x_range=[0, 5, 1], y_range=[0, 5, 1], x_length=7,
                    y_length=5.5, tips=False,
                    y_axis_config={
                        "scaling": LogBase(custom_labels=True)})
        ejes.add_coordinates()
        curva = ejes.plot(lambda x: 10**x, x_range=[0, 5], color=YELLOW,
                          use_smoothing=False)
        rotulo = MathTex(r"y=10^x", color=YELLOW)
        rotulo.next_to(ejes.c2p(3, 10**3), UL)
        aviso = Text("eje y logarítmico", font_size=26, color=GREY_B)
        aviso.next_to(ejes.y_axis, UP)
        self.play(Create(ejes), FadeIn(aviso))
        self.play(Create(curva), Write(rotulo))
