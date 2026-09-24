from manim import *


class RitmoPropio(Scene):
    def construct(self):
        ritmos = [
            ("squish_rate_func(smooth, 0.3, 0.7)",
             squish_rate_func(smooth, 0.3, 0.7)),
            ("not_quite_there(smooth, 0.6)",
             not_quite_there(smooth, 0.6)),
            ("lambda t: np.floor(5 * t) / 5",
             lambda t: np.floor(5 * t) / 5),
            ("lambda t: smooth(t) ** 3",
             lambda t: smooth(t) ** 3),
        ]
        inicio, fin = -1.5, 6.0
        for k, (nombre, funcion) in enumerate(ritmos):
            y = 2.6 - 1.7 * k
            carril = Line([inicio, y, 0], [fin, y, 0], color=GRAY_D)
            rotulo = Text(nombre, font="Monospace", font_size=20)
            rotulo.next_to(carril, LEFT, buff=0.3)
            self.add(carril, rotulo)
            for t in np.linspace(0, 1, 21):
                x = inicio + (fin - inicio) * funcion(t)
                self.add(Dot([x, y, 0], radius=0.07,
                             color=interpolate_color(BLUE, RED, t)))
