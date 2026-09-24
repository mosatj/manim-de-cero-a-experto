from manim import *


class Estroboscopio(Scene):
    def construct(self):
        ritmos = [linear, smooth, rush_into, rush_from,
                  rate_functions.ease_out_bounce]
        inicio, fin = -3.0, 6.2
        for k, funcion in enumerate(ritmos):
            y = 2.8 - 1.4 * k
            carril = Line([inicio, y, 0], [fin, y, 0],
                          color=GRAY_D)
            nombre = Text(funcion.__name__, font="Monospace",
                          font_size=22).next_to(carril, LEFT, 0.3)
            self.add(carril, nombre)
            # 21 instantes igualmente espaciados en el tiempo
            for t in np.linspace(0, 1, 21):
                x = inicio + (fin - inicio) * funcion(t)
                self.add(Dot([x, y, 0], radius=0.07,
                             color=interpolate_color(BLUE, RED, t)))
