from manim import *


class TelaranaLogistica(Scene):
    r = 2.8                    # atributos de clase: los parámetros
    x0 = 0.1
    iteraciones = 30

    def construct(self):
        r = self.r
        f = lambda x: r * x * (1 - x)
        ejes = Axes(x_range=[0, 1, 0.2], y_range=[0, 1, 0.2],
                    x_length=6.5, y_length=6.5, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 22})
        parabola = ejes.plot(f, color=BLUE)
        diagonal = ejes.plot(lambda x: x, color=GRAY)
        self.add(ejes, parabola, diagonal)
        # Telaraña: vertical a la parábola, horizontal a y = x
        x, vertices = self.x0, [ejes.c2p(self.x0, 0)]
        for _ in range(self.iteraciones):
            y = f(x)
            vertices += [ejes.c2p(x, y), ejes.c2p(y, y)]
            x = y
        telarana = VMobject(color=YELLOW, stroke_width=2.5)
        telarana.set_points_as_corners(vertices)
        self.play(Create(telarana), run_time=4, rate_func=linear)
        fijo = 1 - 1 / r                  # punto fijo no nulo
        self.add(Dot(ejes.c2p(fijo, fijo), color=RED))
        derivada = abs(2 - r)             # |f'(x*)| = |r(1 - 2x*)|
        texto = MathTex(rf"r = {r}", rf"|f'(x^*)| = {derivada:.1f}",
                        font_size=34)
        texto.arrange(DOWN, aligned_edge=LEFT)
        self.add(texto.to_corner(UL))


class TelaranaCiclo2(TelaranaLogistica):
    r = 3.2                              # solo cambia el parámetro
