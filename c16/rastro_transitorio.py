from manim import *


def rosa(t):
    # Rosa de tres pétalos: se recorre entera con t en [0, pi]
    r = 1.9 * np.cos(3 * t)
    return np.array([r * np.cos(t), r * np.sin(t), 0])


class RastroTransitorio(Scene):
    def construct(self):
        T = 4                            # segundos de recorrido
        reloj = ValueTracker(0)
        reloj.add_updater(lambda m, dt: m.increment_value(dt))
        self.add(reloj)                  # el reloj, el primero

        def fase():
            return PI * min(reloj.get_value() / T, 1)

        casos = [("sin rastro", None), ("estela de 1 s", 1),
                 ("rastro completo", 0)]
        for k, (nombre, estela) in enumerate(casos):
            centro = (k - 1) * 4.6 * RIGHT + 0.4 * DOWN
            punto = Dot(radius=0.14, color=RED)
            punto.add_updater(
                lambda m, c=centro: m.move_to(c + rosa(fase())))
            punto.update()
            rotulo = Text(nombre, font_size=36)
            self.add(punto, rotulo.move_to(centro + 2.9 * UP))
            if estela is None:
                continue
            opciones = {}
            if estela:                   # 0: rastro permanente
                opciones["dissipating_time"] = estela
            rastro = TracedPath(punto.get_center, stroke_width=4,
                                stroke_color=BLUE, **opciones)
            self.add(rastro)             # después del punto
        self.wait_until(lambda: reloj.get_value() >= T)
