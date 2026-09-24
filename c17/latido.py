from manim import *


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


class EscenaLatido(Scene):
    def construct(self):
        corazon = MathTex(r"\heartsuit", font_size=120, color=RED)
        self.play(Latido(corazon))            # vuelve a su estado
        # Tira de muestras: la misma animación congelada en 5 alphas
        alphas = [0, 0.25, 0.5, 0.75, 1]
        tira = VGroup()
        for a in alphas:
            copia = corazon.copy()
            anim = Latido(copia)
            anim.begin()
            anim.interpolate(a)      # en cualquier orden
            rotulo = MathTex(rf"\alpha={a}", font_size=34)
            tira.add(VGroup(copia, rotulo.next_to(copia, DOWN, .5)))
        tira.arrange(RIGHT, buff=0.7, aligned_edge=DOWN)
        self.remove(corazon)
        self.add(tira)
