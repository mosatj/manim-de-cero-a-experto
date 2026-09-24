from manim import *


def recta_tangente(ejes, f, df, x0, largo=2.2, **estilo):
    """Segmento de la tangente a y = f(x) en x0, de largo fijo."""
    p = ejes.c2p(x0, f(x0))
    # Dirección (1, f'(x0)) medida ya en unidades de la pantalla
    d = ejes.c2p(x0 + 1, f(x0) + df(x0)) - ejes.c2p(x0, f(x0))
    d = d / np.linalg.norm(d)
    return Line(p - largo / 2 * d, p + largo / 2 * d, **estilo)


class TangenteMovil(Scene):
    def construct(self):
        f = lambda x: x * np.sin(x)
        df = lambda x: np.sin(x) + x * np.cos(x)  # derivada exacta
        arriba = Axes(x_range=[0, 6.5, 1], y_range=[-5, 2, 1],
                      x_length=9, y_length=3.2, tips=False)
        abajo = Axes(x_range=[0, 6.5, 1], y_range=[-4, 7, 2],
                     x_length=9, y_length=3.2, tips=False)
        paneles = VGroup(arriba, abajo).arrange(DOWN, buff=0.5)
        paneles.to_edge(LEFT, buff=0.6)
        arriba.add_coordinates(font_size=20)
        abajo.add_coordinates(font_size=20)
        curva = arriba.plot(f, x_range=[0, 6.5], color=BLUE)
        nom_f = MathTex(r"f(x)=x\operatorname{sen}x", color=BLUE)
        nom_df = MathTex(r"f'(x)=\operatorname{sen}x+x\cos x",
                         color=GREEN)
        nom_f.scale(0.65).next_to(arriba, RIGHT).shift(0.8 * UP)
        nom_df.scale(0.65).next_to(abajo, RIGHT).shift(0.8 * UP)

        x = ValueTracker(0)
        tangente = always_redraw(lambda: recta_tangente(
            arriba, f, df, x.get_value(), color=YELLOW))
        punto = always_redraw(lambda: Dot(
            arriba.i2gp(x.get_value(), curva), color=YELLOW))
        # Abajo se dibuja la función «pendiente de la tangente»
        rastro = always_redraw(lambda: abajo.plot(
            df, x_range=[0, x.get_value() + 1e-3], color=GREEN))
        pd = lambda: abajo.c2p(x.get_value(), df(x.get_value()))
        punto_d = always_redraw(lambda: Dot(pd(), color=GREEN))
        guia = always_redraw(lambda: DashedLine(
            punto.get_center(), punto_d.get_center(), color=GRAY))
        valor = DecimalNumber(0, num_decimal_places=2)
        valor.add_updater(lambda m: m.set_value(df(x.get_value())))
        rotulo = VGroup(Text("pendiente =", font_size=26), valor)
        rotulo.arrange(RIGHT).set_color(YELLOW)
        rotulo.next_to(nom_f, DOWN, buff=0.4).align_to(nom_f, LEFT)

        self.play(Create(arriba), Create(abajo), Create(curva),
                  Write(nom_f), Write(nom_df))
        self.play(FadeIn(tangente, punto, punto_d, guia, rotulo))
        self.add(rastro)
        self.play(x.animate.set_value(2.03), run_time=2)
        self.play(x.animate.set_value(4.91), run_time=3)
        self.play(x.animate.set_value(6.3), run_time=2)
