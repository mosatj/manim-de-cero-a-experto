from manim import *


class FamiliaParabolas(Scene):
    def construct(self):
        ejes = Axes(x_range=[-4, 4, 1], y_range=[-2, 6, 1],
                    x_length=8, y_length=6, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 24})
        ejes.to_edge(LEFT, buff=0.8)
        a = ValueTracker(-2)          # el parámetro de la familia

        def parabola():
            h = a.get_value()
            return ejes.plot(lambda x: (x - h) ** 2 - 1,
                             x_range=[h - 2.6, h + 2.6], color=BLUE)

        curva = always_redraw(parabola)
        vertice = always_redraw(lambda: Dot(
            ejes.c2p(a.get_value(), -1), color=YELLOW))
        valor = DecimalNumber(a.get_value(), num_decimal_places=1)
        valor.add_updater(lambda d: d.set_value(a.get_value()))
        rotulo = VGroup(MathTex("a ="), valor).arrange(RIGHT)
        rotulo.to_edge(RIGHT, buff=1).shift(UP * 1.5)
        formula = MathTex(r"y=(x-a)^2-1")
        formula.next_to(rotulo, DOWN, aligned_edge=RIGHT)
        self.add(ejes, curva, vertice, rotulo, formula)
        self.play(a.animate.set_value(1.5), run_time=2)
        self.play(a.animate.set_value(-0.5), run_time=1.5)
        self.play(a.animate.set_value(0.8), run_time=1)
        self.wait()
