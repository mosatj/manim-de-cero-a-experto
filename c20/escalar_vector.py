from manim import *


class EscalarVector(Scene):
    def construct(self):
        plano = NumberPlane()
        v = np.array([2, 1, 0])
        c = ValueTracker(1)
        # c·v se redibuja en cada fotograma; la recta queda fija
        recta = Line(-4 * v, 4 * v, color=GRAY, stroke_width=2)
        cv = always_redraw(lambda: Vector(c.get_value() * v,
                                          color=YELLOW))
        valor = DecimalNumber(1, num_decimal_places=2,
                              include_sign=True)
        valor.add_updater(lambda m: m.set_value(c.get_value()))
        rotulo = VGroup(MathTex("c ="), valor).arrange(RIGHT)
        rotulo.add_background_rectangle().to_corner(UL)

        self.add(plano, recta, cv, rotulo)
        self.play(c.animate.set_value(2.5), run_time=2)
        self.play(c.animate.set_value(-1.5), run_time=3)
