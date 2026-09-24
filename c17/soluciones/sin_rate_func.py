from manim import *


class ContadorBien(Animation):
    def __init__(self, numero, fin, **kwargs):
        super().__init__(numero, suspend_mobject_updating=False,
                         **kwargs)
        self.fin = fin

    def interpolate_mobject(self, alpha):
        self.mobject.set_value(self.rate_func(alpha) * self.fin)


class ContadorMal(ContadorBien):
    def interpolate_mobject(self, alpha):
        self.mobject.set_value(alpha * self.fin)  # olvida rate_func


class SinRateFunc(Scene):
    def construct(self):
        ritmo = rate_functions.ease_in_expo
        columnas = VGroup()
        for clase in (ContadorBien, ContadorMal):
            numero = DecimalNumber(0, font_size=80)
            anim = clase(numero, 100, rate_func=ritmo)
            anim.begin()
            anim.interpolate(0.5)          # a mitad de tiempo
            nombre = Text(clase.__name__, font="Menlo",
                          font_size=28)
            columna = VGroup(nombre, numero).arrange(DOWN, buff=0.5)
            columnas.add(columna)
        columnas.arrange(RIGHT, buff=2.5)
        pie = MathTex(r"\alpha=0.5,\quad",
                      r"\texttt{ease\_in\_expo}(0.5)",
                      r"=2^{-5}=0.03125", font_size=36)
        pie.next_to(columnas, DOWN, buff=1)
        self.add(columnas, pie)
