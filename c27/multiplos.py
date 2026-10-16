from manim import *

FRECUENCIAS = [1, 2, 3, 4]
EJES = dict(x_range=[0, 8, 2], y_range=[-1, 1, 1], tips=False)


def onda(plano, w, color):
    return plano.plot(lambda x: np.exp(-0.2 * x) * np.cos(w * x),
                      x_range=[0, 8, 0.02], color=color)


class MultiplosAntes(Scene):
    def construct(self):
        plano = Axes(x_length=11, y_length=6, **EJES)
        colores = [RED, GREEN, BLUE, PURPLE]
        curvas = VGroup(*[onda(plano, w, c)
                          for w, c in zip(FRECUENCIAS, colores)])
        leyenda = VGroup(*[
            VGroup(Line(ORIGIN, 0.6 * RIGHT, color=c),
                   MathTex(rf"\omega={w}")).arrange(RIGHT)
            for w, c in zip(FRECUENCIAS, colores)])
        leyenda.arrange(DOWN, aligned_edge=LEFT).to_corner(UR)
        self.play(Create(plano), Create(curvas), FadeIn(leyenda))


def panel(w):
    plano = Axes(x_length=5.6, y_length=2.6, **EJES)  # misma escala
    envolvente = DashedVMobject(plano.plot(lambda x: np.exp(-0.2 * x),
                                           x_range=[0, 8]))
    envolvente.set_stroke(GRAY, 3)  # la misma referencia en todos
    nombre = MathTex(rf"\omega={w}", font_size=44)
    nombre.next_to(plano, UP, buff=0.1).align_to(plano, RIGHT)
    return VGroup(plano, envolvente, onda(plano, w, BLUE), nombre)


class MultiplosDespues(Scene):
    def construct(self):
        paneles = VGroup(*[panel(w) for w in FRECUENCIAS])
        paneles.arrange_in_grid(rows=2, cols=2, buff=(0.9, 0.5))
        self.play(LaggedStart(*[Create(p) for p in paneles],
                              lag_ratio=0.3))
