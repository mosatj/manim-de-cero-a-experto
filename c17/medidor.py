from manim import *


class Medidor(VGroup):
    """Barra de progreso con su porcentaje; valor entre 0 y 100."""

    def __init__(self, valor=0, ancho=8, alto=0.5, color=GREEN,
                 **kwargs):
        super().__init__(**kwargs)
        self.ancho, self.valor = ancho, valor
        self.marco = RoundedRectangle(corner_radius=alto / 2,
                                      width=ancho, height=alto,
                                      color=GRAY_B)
        self.barra = Rectangle(width=ancho, height=alto * 0.7,
                               stroke_width=0, fill_color=color,
                               fill_opacity=1)
        self.cifra = DecimalNumber(valor, num_decimal_places=0,
                                   unit=r"\%", font_size=40)
        self.add(self.marco, self.barra, self.cifra)
        self._colocar()

    def _colocar(self):
        # Todo se deduce de self.valor: dibujar = función del estado
        izquierda = self.marco.get_left() + RIGHT * 0.1
        largo = max(self.valor / 100 * (self.ancho - 0.2), 1e-3)
        self.barra.stretch_to_fit_width(largo)
        self.barra.move_to(izquierda, aligned_edge=LEFT)
        self.cifra.set_value(self.valor)
        self.cifra.next_to(self.marco, RIGHT, buff=0.3)
        return self

    def fijar_valor(self, valor):
        self.valor = valor
        return self._colocar()

    @override_animate(fijar_valor)
    def _animar_fijar_valor(self, valor, anim_args=None):
        # medidor.animate.fijar_valor(v) llega aquí
        inicio = self.valor
        def paso(m, a):
            m.fijar_valor(interpolate(inicio, valor, a))
        return UpdateFromAlphaFunc(self, paso, **(anim_args or {}))


class EscenaMedidor(Scene):
    def construct(self):
        colores = (BLUE, GREEN, RED)
        medidores = VGroup(*[Medidor(color=c) for c in colores])
        medidores.arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        medidores.shift(LEFT * 0.6)
        self.add(medidores)
        m0, m1, m2 = medidores
        self.play(m0.animate.fijar_valor(35),
                  m1.animate(run_time=2).fijar_valor(80),
                  m2.animate(rate_func=linear).fijar_valor(100))
        self.wait()
