from manim import *


class RosasPolares(Scene):
    def construct(self):
        theta = ValueTracker(0.001)
        paneles = VGroup()
        for k in (1, 2, 3, 4):
            ejes = Axes(x_range=[-1.2, 1.2], y_range=[-1.2, 1.2],
                        x_length=3, y_length=3, tips=False,
                        axis_config={"stroke_opacity": 0.4,
                                     "include_ticks": False})
            titulo = MathTex(rf"r = \cos {k}\theta" if k > 1
                             else r"r = \cos\theta", font_size=34)
            paneles.add(VGroup(ejes, titulo.next_to(ejes, UP, 0.1)))
        paneles.arrange(RIGHT, buff=0.5).shift(0.3 * DOWN)
        for k, (ejes, _) in zip((1, 2, 3, 4), paneles):
            # La curva es función PURA del tracker: 0 <= t <= theta
            curva = always_redraw(
                lambda e=ejes, k=k: e.plot_polar_graph(
                    lambda t: np.cos(k * t),
                    theta_range=[0, theta.get_value()],
                    color=YELLOW))
            def punto_en(e, k):
                t = theta.get_value()
                return Dot(e.polar_to_point(np.cos(k * t), t),
                           radius=0.05, color=RED)
            punto = always_redraw(
                lambda e=ejes, k=k: punto_en(e, k))
            self.add(curva, punto)
        self.add(paneles)
        self.play(theta.animate.set_value(TAU), run_time=6,
                  rate_func=linear)
