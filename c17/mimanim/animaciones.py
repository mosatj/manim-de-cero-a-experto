"""Animaciones propias de mimanim (capítulo 17)."""
from manim import *

__all__ = ["Contador", "SubirYAparecer", "DibujarConLapiz",
           "Latido"]


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


class SubirYAparecer(Animation):
    """Cada pieza sube un poco y se vuelve opaca, una tras otra."""

    def __init__(self, mob, altura=0.4, lag_ratio=0.08, **kwargs):
        super().__init__(mob, lag_ratio=lag_ratio,
                         introducer=True, **kwargs)
        self.altura = altura

    def interpolate_submobject(self, sub, ini, alpha):
        # alpha ya viene con la rate_func y el retraso de esta pieza
        bajada = (1 - alpha) * self.altura * DOWN
        sub.points = ini.points + bajada
        sub.set_fill(opacity=alpha * ini.get_fill_opacity())
        sub.set_stroke(opacity=alpha * ini.get_stroke_opacity())


class DibujarConLapiz(Animation):
    """Como Create, pero con un «lápiz» luminoso en la punta."""

    def __init__(self, curva, color_lapiz=YELLOW, quitar_lapiz=True,
                 **kwargs):
        self.curva = curva
        self.lapiz = Dot(radius=0.09, color=color_lapiz)
        self.halo = Dot(radius=0.22, color=color_lapiz,
                        fill_opacity=0.3)
        self.quitar_lapiz = quitar_lapiz
        # El mobject de la animación es el grupo curva + lápiz
        grupo = VGroup(curva, self.halo, self.lapiz)
        super().__init__(grupo, introducer=True, **kwargs)

    def interpolate_mobject(self, alpha):
        t = self.rate_func(alpha)
        curva_inicial = self.starting_mobject[0]
        self.curva.pointwise_become_partial(curva_inicial, 0, t)
        punta = curva_inicial.point_from_proportion(t)
        self.lapiz.move_to(punta)
        self.halo.move_to(punta)

    def clean_up_from_scene(self, scene):
        super().clean_up_from_scene(scene)
        if self.quitar_lapiz:
            scene.remove(self.mobject)  # quita el grupo completo...
            scene.add(self.curva)        # ...y deja solo la curva


class Latido(Animation):
    """Crece, se tiñe y vuelve exactamente a su estado."""

    def __init__(self, mobject, escala=1.35, color=YELLOW,
                 rate_func=there_and_back, **kwargs):
        super().__init__(mobject, rate_func=rate_func, **kwargs)
        self.escala = escala
        self.color = color

    def interpolate_mobject(self, alpha):
        t = self.rate_func(alpha)            # 0 -> 1 -> 0
        # Patrón «reiniciar y aplicar»: nada se acumula
        self.mobject.become(self.starting_mobject)
        self.mobject.scale(1 + (self.escala - 1) * t)
        piezas = self.mobject.family_members_with_points()
        inicial = self.starting_mobject.family_members_with_points()
        for sub, ini in zip(piezas, inicial):
            sub.set_color(interpolate_color(ini.get_color(),
                                            self.color, t))
