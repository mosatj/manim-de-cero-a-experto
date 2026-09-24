from manim import *


class Reloj(VGroup):
    """Reloj analógico; poner_hora(h, m) mueve las agujas."""

    def __init__(self, radio=2, hora=12, minuto=0, **kwargs):
        super().__init__(**kwargs)
        self.esfera = Circle(radius=radio, color=GRAY_B)
        marcas = VGroup(*[
            Line(radio * 0.85 * UP, radio * UP, stroke_width=3)
            .rotate(-k * TAU / 12, about_point=ORIGIN)
            for k in range(12)])
        self.horario = Line(ORIGIN, radio / 2 * UP, stroke_width=8)
        self.minutero = Line(ORIGIN, 0.8 * radio * UP, color=YELLOW)
        self.minutero.set_stroke(width=5)
        self.add(self.esfera, marcas, self.horario, self.minutero,
                 Dot(radius=0.08))
        self.minutos = 0                 # minutos desde las 12:00
        self.poner_hora(hora, minuto)

    def _angulos(self, minutos):
        # Ángulos en sentido horario desde las 12
        return -TAU * minutos / 720, -TAU * minutos / 60

    def poner_hora(self, hora, minuto):
        nuevos = (hora % 12) * 60 + minuto
        self._girar(nuevos - self.minutos)
        return self

    def _girar(self, delta):
        a_h, a_m = self._angulos(delta)
        centro = self.esfera.get_center()
        self.horario.rotate(a_h, about_point=centro)
        self.minutero.rotate(a_m, about_point=centro)
        self.minutos += delta

    @override_animate(poner_hora)
    def _animar_poner_hora(self, hora, minuto, anim_args=None):
        # Las agujas avanzan girando, siempre hacia delante
        destino = (hora % 12) * 60 + minuto
        delta = (destino - self.minutos) % 720
        inicio = self.minutos

        def paso(reloj, t):
            reloj._girar(inicio + t * delta - reloj.minutos)

        return UpdateFromAlphaFunc(self, paso, **(anim_args or {}))


class EscenaReloj(Scene):
    def construct(self):
        ingenuo = Reloj(hora=3).shift(LEFT * 3.3)
        propio = Reloj(hora=3).shift(RIGHT * 3.3)
        rotulos = VGroup(Text("Transform genérico", font_size=28),
                         Text("override_animate", font_size=28))
        rotulos[0].next_to(ingenuo, DOWN)
        rotulos[1].next_to(propio, DOWN)
        self.add(ingenuo, propio, rotulos)
        # Mismo destino (9:45), dos caminos muy distintos
        plana = Transform(ingenuo, ingenuo.copy().poner_hora(9, 45))
        a_medida = propio.animate.poner_hora(9, 45).build()
        # Último fotograma: ambas congeladas a mitad de camino
        for anim in (plana, a_medida):
            anim.begin()
            anim.interpolate(0.5)
        self.add(Text("alpha = 0.5", font_size=30, color=GRAY_B)
                 .to_edge(UP))
