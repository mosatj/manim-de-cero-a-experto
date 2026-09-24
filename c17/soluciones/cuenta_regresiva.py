from manim import *


class Contador(Animation):
    def __init__(self, numero, inicio, fin, **kwargs):
        kwargs.setdefault("suspend_mobject_updating", False)
        super().__init__(numero, **kwargs)
        self.inicio, self.fin = inicio, fin

    def interpolate_mobject(self, alpha):
        t = self.rate_func(alpha)
        valor = self.inicio + t * (self.fin - self.inicio)
        self.mobject.set_value(valor)


class CuentaRegresiva(Scene):
    def construct(self):
        numero = Integer(10, font_size=160, color=YELLOW)
        numero.add_updater(lambda m: m.move_to(ORIGIN))
        self.add(numero)
        # Integer redondea: con linear cada número dura lo mismo
        self.play(Contador(numero, 10, 0), run_time=5,
                  rate_func=linear)
        mensaje = Text("¡Despegue!", font_size=64, color=RED)
        self.play(ReplacementTransform(numero, mensaje))
        self.wait()
