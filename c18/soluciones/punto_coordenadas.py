from manim import *


class PuntoCoordenadas(Scene):
    def construct(self):
        ejes = Axes(x_range=[-3, 3, 1], y_range=[-1, 5, 1],
                    x_length=8, y_length=6, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 24})
        f = lambda x: 0.5 * x ** 2
        curva = ejes.plot(f, color=BLUE)
        x = ValueTracker(-2.5)

        def punto_actual():
            return ejes.c2p(x.get_value(), f(x.get_value()))

        punto = always_redraw(lambda: Dot(punto_actual(),
                                          color=YELLOW))
        lineas = always_redraw(lambda: ejes.get_lines_to_point(
            punto_actual(), color=YELLOW))
        cx = DecimalNumber(0, num_decimal_places=2)
        cy = DecimalNumber(0, num_decimal_places=2)
        cx.add_updater(lambda d: d.set_value(x.get_value()))
        cy.add_updater(lambda d: d.set_value(f(x.get_value())))
        lectura = VGroup(MathTex("x="), cx, MathTex(r",\ y="), cy)
        lectura.arrange(RIGHT, buff=0.1).to_corner(UL)
        self.add(ejes, curva, lineas, punto, lectura)
        self.play(x.animate.set_value(2.2), run_time=4)
        self.wait()
