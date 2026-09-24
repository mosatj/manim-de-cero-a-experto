from manim import *

# Okabe e Ito: distinguibles con los tipos de daltonismo comunes
NARANJA, AZUL_CIELO, BERMELLON = "#E69F00", "#56B4E9", "#D55E00"


def ejes():
    return Axes(x_range=[0, 6], y_range=[0, 6], x_length=6.5,
                y_length=4.5).shift(LEFT)


class ColorAntes(Scene):
    def construct(self):
        e = ejes()
        a = e.plot(lambda x: 0.8 * x + 0.5, color=PURE_RED)
        b = e.plot(lambda x: 5.5 - 0.7 * x, color=PURE_GREEN)
        leyenda = VGroup(
            Text("■ oferta", font_size=26, color=PURE_RED),
            Text("■ demanda", font_size=26, color=PURE_GREEN),
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UR)
        self.play(Create(e), Create(a), Create(b), FadeIn(leyenda))


class ColorDespues(Scene):
    def construct(self):
        e = ejes()
        a = e.plot(lambda x: 0.8 * x + 0.5, color=NARANJA)
        b = DashedVMobject(e.plot(lambda x: 5.5 - 0.7 * x,
                                  color=AZUL_CIELO), num_dashes=30)
        # Rótulos directos: el nombre junto a la curva, sin leyenda
        ra = Text("oferta", font_size=30, color=NARANJA)
        ra.next_to(e.c2p(6, 5.3), RIGHT)
        rb = Text("demanda", font_size=30, color=AZUL_CIELO)
        rb.next_to(e.c2p(6, 1.3), RIGHT)
        x0 = 5 / 1.5
        corte = Dot(e.c2p(x0, 0.8 * x0 + 0.5), color=WHITE)
        self.play(Create(e), Create(a), Create(b))
        self.play(FadeIn(ra), FadeIn(rb), GrowFromCenter(corte))
