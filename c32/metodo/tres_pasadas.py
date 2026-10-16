from manim import *

# Pasada 1: dónde va cada cosa. Las siguientes no lo mueven.
ZONA_EJES = Rectangle(width=6.5, height=5).shift(3.2 * LEFT)
ZONA_FORMULA = Rectangle(width=5.5, height=2.2).shift(3.6 * RIGHT)


def plano(pasada):
    """El mismo plano en la pasada 1, 2 o 3."""
    if pasada == 1:  # bloques: solo la composición
        bloques = VGroup(ZONA_EJES.copy(), ZONA_FORMULA.copy())
        return bloques.set_stroke(GRAY, 6)
    ejes = Axes(x_range=[0, 2, 1], y_range=[0, 4, 1], x_length=6.5,
                y_length=5, tips=False).move_to(ZONA_EJES)
    curva = ejes.plot(lambda x: x**2)
    area = ejes.get_area(curva, x_range=[0, 2])
    formula = MathTex(r"\int_0^2 x^2\,dx", "=", r"\frac{8}{3}",
                      font_size=96).move_to(ZONA_FORMULA)
    if pasada == 2:  # objetos reales en su sitio, sin acabado
        area.set_fill(GRAY, opacity=0.2)
        return VGroup(ejes, area, curva, formula).set_color(GRAY)
    curva.set_color(BLUE_D)  # pasada 3: color y énfasis
    area.set_fill(BLUE_D, opacity=0.5)
    formula[2].set_color(RED_D)
    return VGroup(ejes, area, curva, formula)


class TresPasadas(Scene):
    def construct(self):
        nombres = ["composición", "objetos", "acabado"]
        paneles = VGroup()
        for n, nombre in enumerate(nombres, start=1):
            marco = Rectangle(width=14.2, height=8, color=GRAY_D)
            panel = VGroup(marco, plano(n)).scale(0.3)
            rotulo = Text(f"{n}. {nombre}", font_size=30)
            paneles.add(VGroup(panel, rotulo.next_to(panel, DOWN)))
        paneles.arrange(RIGHT, buff=0.3, aligned_edge=UP)
        self.play(LaggedStart(*[FadeIn(p) for p in paneles],
                              lag_ratio=0.5))
        self.wait()
