from manim import *
from math import factorial

config.frame_height = 4.6
config.pixel_height = round(config.pixel_width * 4.6 / config.frame_width)


def taylor_seno(n):
    """Polinomio de Taylor de sen x de grado n alrededor de 0."""
    return lambda x: sum((-1)**k * x**(2 * k + 1) / factorial(2 * k + 1)
                         for k in range((n + 1) // 2))


class AreaUniversidad(Scene):
    def construct(self):
        ejes = Axes(x_range=[-7, 7, 1], y_range=[-2, 2, 1], x_length=10,
                    y_length=3.8, tips=False).shift(LEFT * 1.6)

        def hasta_salir(f, limite=2.0):
            """Mayor x > 0 hasta el que |f| no sale de la ventana."""
            xs = np.linspace(0, 7, 1401)
            fuera = np.nonzero(np.abs([f(x) for x in xs]) > limite)[0]
            return xs[fuera[0]] if len(fuera) else 7.0
        seno = ejes.plot(np.sin, color=GREY_B, stroke_width=7)
        grados = [1, 3, 5, 7, 9]
        tonos = [BLUE_D, TEAL_D, GREEN_D, PURPLE_D, RED_D]
        curvas = VGroup()
        for n, tono in zip(grados, tonos):
            p = taylor_seno(n)
            x_max = hasta_salir(p)  # p es impar: el intervalo es simétrico
            curvas.add(ejes.plot(p, x_range=[-x_max, x_max, 0.02],
                                 color=tono, stroke_width=3))
        leyenda = VGroup(MathTex(r"\sin x", color=GREY_B, font_size=40),
                         *[MathTex(rf"P_{{{n}}}", color=tono, font_size=40)
                           for n, tono in zip(grados, tonos)])
        leyenda.arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        leyenda.next_to(ejes, RIGHT, buff=0.5)
        self.play(Create(ejes), Create(seno), Write(leyenda[0]))
        for curva, rotulo in zip(curvas, leyenda[1:]):  # un grado cada vez
            self.play(Create(curva), FadeIn(rotulo), run_time=1.2)
        self.add_foreground_mobject(seno)  # la función, siempre encima
        self.wait()
