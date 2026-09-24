from manim import *


class ContadorHeredado(ChangingDecimal):
    """El Contador del capítulo, reutilizando ChangingDecimal."""

    def __init__(self, numero, inicio, fin, **kwargs):
        # ChangingDecimal ya aplica rate_func y no suspende updaters
        def valor(t):
            return interpolate(inicio, fin, t)
        super().__init__(numero, valor, **kwargs)


class EscenaHeredado(Scene):
    def construct(self):
        numero = Integer(0, font_size=120)
        numero.add_updater(lambda m: m.move_to(ORIGIN))
        self.add(numero)
        self.play(ContadorHeredado(numero, 0, 2026), run_time=3)
        self.wait()
