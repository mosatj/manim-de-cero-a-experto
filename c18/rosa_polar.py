from manim import *


class RosaPolar(Scene):
    def construct(self):
        plano = PolarPlane(radius_max=3, size=6.5,
                           azimuth_units="PI radians",
                           azimuth_step=8,
                           background_line_style={
                               "stroke_color": BLUE_E,
                               "stroke_opacity": 0.6})
        plano.add_coordinates()
        # plot_polar_graph recibe r(theta)
        rosa = plano.plot_polar_graph(lambda th: 3 * np.cos(4 * th),
                                      [0, TAU], color=YELLOW)
        cardioide = plano.plot_polar_graph(
            lambda th: 1.2 * (1 + np.cos(th)), [0, TAU], color=RED)
        formulas = VGroup(
            MathTex(r"r=3\cos 4\theta", color=YELLOW),
            MathTex(r"r=1.2\,(1+\cos\theta)", color=RED),
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UR)
        self.add(plano)
        self.play(Create(rosa), run_time=3)
        self.play(Create(cardioide), FadeIn(formulas))
        self.wait()
