from manim import *


class CirculoUnitario(Scene):
    def construct(self):
        R, O = 1.8, np.array([-4, 0, 0])    # radio y centro
        circulo = Circle(radius=R, color=GRAY).move_to(O)
        ejes = Axes(x_range=[0, TAU, PI / 2], y_range=[-1, 1, 1],
                    x_length=7, y_length=2 * R, tips=False)
        ejes.next_to(circulo, RIGHT, buff=1.2)
        theta = ValueTracker(0.01)
        P = lambda: O + R * np.array([np.cos(theta.get_value()),
                                      np.sin(theta.get_value()), 0])
        radio = always_redraw(lambda: Line(O, P(), color=WHITE))
        seno = always_redraw(lambda: Line(      # cateto vertical
            [P()[0], O[1], 0], P(), color=RED, stroke_width=6))
        coseno = always_redraw(lambda: Line(    # cateto horizontal
            O, [P()[0], O[1], 0], color=BLUE, stroke_width=6))
        arco = always_redraw(lambda: Arc(
            0.5, 0, theta.get_value(), arc_center=O, color=YELLOW))
        onda = always_redraw(lambda: ejes.plot(
            np.sin, x_range=[0, theta.get_value()], color=RED))
        Q = lambda: ejes.c2p(theta.get_value(),
                             np.sin(theta.get_value()))
        enlace = always_redraw(
            lambda: DashedLine(P(), Q(), color=GRAY))
        punto = always_redraw(lambda: Dot(P(), color=YELLOW))
        self.add(circulo, ejes, radio, coseno, seno, arco, onda,
                 enlace, punto)
        for fin in (PI / 2, PI, 3 * PI / 2, TAU):
            self.play(theta.animate.set_value(fin), run_time=2,
                      rate_func=linear)
