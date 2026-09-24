from manim import *


class AreaSenoCoseno(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 2 * PI, PI / 4],
                    y_range=[-1.5, 1.5, 1], x_length=10, y_length=4.5, tips=False)
        seno = ejes.plot(np.sin, color=BLUE)
        coseno = ejes.plot(np.cos, color=RED)
        # Entre pi/4 y 5pi/4 el seno queda por encima del coseno
        region = ejes.get_area(seno, x_range=(PI / 4, 5 * PI / 4),
                               bounded_graph=coseno, color=YELLOW,
                               opacity=0.4)
        valor = MathTex(r"\int_{\pi/4}^{5\pi/4}(\sin x-\cos x)\,dx"
                        r"=2\sqrt{2}")
        valor.to_edge(UP)
        self.add(ejes, seno, coseno)
        self.play(FadeIn(region), Write(valor))
        self.wait()
