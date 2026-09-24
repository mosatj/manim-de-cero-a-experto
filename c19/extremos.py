from manim import *

from tangente_movil import recta_tangente   # misma utilidad


class Extremos(Scene):
    def construct(self):
        f = lambda x: x**3 - 3 * x
        df = lambda x: 3 * x**2 - 3
        ejes = Axes(x_range=[-2.2, 2.2, 1], y_range=[-4, 4, 2],
                    x_length=8, y_length=5, tips=False)
        ejes.add_coordinates(font_size=22).to_edge(UP, buff=0.3)
        # Crece en verde (f' > 0) y decrece en rojo (f' < 0)
        tramos = VGroup(
            ejes.plot(f, x_range=[-2.2, -1], color=GREEN),
            ejes.plot(f, x_range=[-1, 1], color=RED),
            ejes.plot(f, x_range=[1, 2.2], color=GREEN))

        x = ValueTracker(-2)
        def color_pendiente():
            m = df(x.get_value())
            if abs(m) < 0.15:                  # casi horizontal
                return YELLOW
            return GREEN if m > 0 else RED
        tangente = always_redraw(lambda: recta_tangente(
            ejes, f, df, x.get_value(), largo=2.5,
            color=color_pendiente()))

        # Tabla de signos de f'(x) = 3(x − 1)(x + 1)
        recta = NumberLine(x_range=[-2.2, 2.2, 1], length=8,
                           include_ticks=False)
        recta.to_edge(DOWN, buff=1)
        marcas = VGroup(*[MathTex(t, font_size=34).next_to(
            recta.n2p(v), DOWN) for t, v in [("-1", -1), ("1", 1)]])
        signos = VGroup(*[MathTex(s, color=c).next_to(
            recta.n2p(v), UP) for s, v, c in
            [("+", -1.6, GREEN), ("-", 0, RED), ("+", 1.6, GREEN)]])
        cortes = VGroup(*[Dot(recta.n2p(v)) for v in (-1, 1)])
        nombre = MathTex(r"\text{signo } f'(x)", font_size=34)
        nombre.next_to(recta, LEFT)
        tabla = VGroup(recta, marcas, signos, cortes, nombre)

        extremos = VGroup()
        for v, texto, lado in [(-1, "máximo local", UP),
                               (1, "mínimo local", DOWN)]:
            horizontal = recta_tangente(ejes, f, df, v, largo=2.5,
                                        color=YELLOW)
            punto = Dot(ejes.c2p(v, f(v)), color=YELLOW)
            rotulo = Text(texto, font_size=24).next_to(punto, lado)
            extremos.add(VGroup(horizontal, punto, rotulo))

        self.play(Create(ejes), Create(tramos))
        self.play(FadeIn(tangente), FadeIn(tabla))
        self.play(x.animate.set_value(2), run_time=5)
        self.play(FadeOut(tangente), FadeIn(extremos))
