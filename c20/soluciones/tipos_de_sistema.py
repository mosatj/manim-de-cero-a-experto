from manim import *


class TiposDeSistema(Scene):
    def construct(self):
        casos = [
            # (función, color, dominio para no salir de los ejes)
            ("una solución", [(lambda x: 5 - 2*x, YELLOW, [0.5, 3]),
                              (lambda x: x - 1, BLUE, [0, 4])]),
            ("ninguna", [(lambda x: 1 - x, YELLOW, [-1, 2]),
                         (lambda x: 3 - x, BLUE, [-1, 4])]),
            ("infinitas", [(lambda x: 2 - x / 2, YELLOW, [-1, 4]),
                           (lambda x: 2 - x / 2, BLUE, [-1, 4])])]
        paneles = VGroup()
        for titulo, rectas in casos:
            ejes = Axes(x_range=[-1, 4], y_range=[-1, 4],
                        x_length=3.8, y_length=3.8, tips=False)
            grafs = VGroup(*[ejes.plot(f, x_range=d, color=c,
                                       stroke_width=w)
                             for (f, c, d), w
                             in zip(rectas, (8, 3))])
            nombre = Text(titulo, font_size=28).next_to(ejes, DOWN)
            paneles.add(VGroup(ejes, grafs, nombre))
        paneles.arrange(RIGHT, buff=0.6)
        self.add(paneles)
