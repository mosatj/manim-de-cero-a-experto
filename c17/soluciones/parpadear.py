from manim import *


class Parpadear(Animation):
    """Apaga y enciende `veces` veces; acaba como empezó."""

    def __init__(self, mobject, veces=3, minimo=0.1, **kwargs):
        kwargs.setdefault("rate_func", linear)
        super().__init__(mobject, **kwargs)
        self.veces, self.minimo = veces, minimo

    def interpolate_mobject(self, alpha):
        t = self.rate_func(alpha)
        # 1 en t = 0 y t = 1; mínimo en medio de cada parpadeo
        onda = np.sin(PI * self.veces * t) ** 2
        factor = 1 - (1 - self.minimo) * onda
        piezas = self.mobject.family_members_with_points()
        inicial = self.starting_mobject.family_members_with_points()
        for sub, ini in zip(piezas, inicial):
            sub.set_fill(opacity=factor * ini.get_fill_opacity())
            sub.set_stroke(opacity=factor*ini.get_stroke_opacity())


class EscenaParpadear(Scene):
    def construct(self):
        aviso = VGroup(
            Triangle(color=YELLOW, fill_opacity=0.3).scale(1.5),
            Text("!", font_size=96, color=YELLOW).shift(DOWN * 0.2))
        self.add(aviso)
        self.play(Parpadear(aviso, veces=4), run_time=2)
        self.wait()
