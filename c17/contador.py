from manim import *


class Contador(Animation):
    """Un DecimalNumber que cuenta desde `inicio` hasta `fin`."""

    def __init__(self, numero, inicio, fin, **kwargs):
        kwargs.setdefault("suspend_mobject_updating", False)
        super().__init__(numero, **kwargs)
        self.inicio = inicio
        self.fin = fin

    def interpolate_mobject(self, alpha):
        # Al redefinir interpolate_mobject, la rate_func va a mano
        t = self.rate_func(alpha)
        valor = self.inicio + t * (self.fin - self.inicio)
        self.mobject.set_value(valor)


class EscenaContador(Scene):
    def construct(self):
        numero = DecimalNumber(0, num_decimal_places=1, unit=r"\%",
                               font_size=120, color=YELLOW)
        numero.add_updater(lambda m: m.move_to(ORIGIN))
        rotulo = Text("de respuestas correctas", font_size=36)
        rotulo.next_to(ORIGIN, DOWN, buff=1.2)
        self.add(numero, rotulo)
        self.play(Contador(numero, 0, 87.5), run_time=3)
        self.wait()
