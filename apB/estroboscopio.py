from manim import *


class Estroboscopio(Scene):
    def construct(self):
        # Cada fila: la posición x = f(t) en 21 instantes
        rebote = rate_functions.ease_out_bounce
        ritmos = [("linear", linear), ("smooth", smooth),
                  ("rush_into", rush_into),
                  ("rush_from", rush_from),
                  ("running_start", running_start),
                  ("ease_out_bounce", rebote)]
        inicio, fin = -3.5, 5.5
        for fila, (nombre, f) in enumerate(ritmos):
            y = 2.9 - 1.15 * fila
            carril = Line([inicio, y, 0], [fin, y, 0], color=GRAY_D)
            rotulo = Text(nombre, font="Menlo", font_size=26)
            rotulo.next_to(carril, LEFT, buff=0.4)
            puntos = VGroup()
            for k in range(21):
                t = k / 20
                x = interpolate(inicio, fin, f(t))
                # el color codifica el instante t (de BLUE a YELLOW)
                color = interpolate_color(BLUE, YELLOW, t)
                puntos.add(Dot([x, y, 0], radius=0.07, color=color))
            self.add(carril, rotulo, puntos)
