from manim import *


class Semaforo(VGroup):
    COLORES = [RED, YELLOW, GREEN]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        caja = RoundedRectangle(width=1.6, height=4.2,
                                corner_radius=0.3, color=GREY_B,
                                fill_opacity=0.25)
        luces = VGroup(*[
            Circle(radius=0.55, color=c, fill_opacity=0.15)
            for c in self.COLORES]).arrange(DOWN, buff=0.25)
        self.add(caja, luces)
        self.luces = luces               # atajo con nombre propio

    def encender(self, i):
        for k, luz in enumerate(self.luces):
            luz.set_fill(opacity=1 if k == i else 0.15)
        return self


class EscenaSemaforos(Scene):
    def construct(self):
        s = VGroup(*[Semaforo() for _ in range(3)])
        s.arrange(RIGHT, buff=1)
        self.play(FadeIn(s))
        for i, semaforo in enumerate(s):
            self.play(semaforo.animate.encender(i), run_time=0.6)
