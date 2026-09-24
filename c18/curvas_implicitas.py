from manim import *


class CurvasImplicitas(Scene):
    def construct(self):
        plano = NumberPlane(x_range=[-4, 4, 1], y_range=[-3, 3, 1],
                            x_length=9, y_length=6.75,
                            background_line_style={
                                "stroke_opacity": 0.4})
        plano.add_coordinates(font_size=22)
        # plot_implicit_curve dibuja F(x, y) = 0
        folium = plano.plot_implicit_curve(
            lambda x, y: x ** 3 + y ** 3 - 3 * x * y, color=YELLOW)
        lemniscata = plano.plot_implicit_curve(
            lambda x, y: (x**2 + y**2) ** 2 - 4 * (x**2 - y**2),
            color=RED)
        formulas = VGroup(
            MathTex(r"x^3+y^3=3xy", color=YELLOW),
            MathTex(r"(x^2+y^2)^2=4(x^2-y^2)", color=RED),
        ).arrange(DOWN, aligned_edge=LEFT)
        formulas.add_background_rectangle(opacity=0.85, buff=0.15)
        formulas.to_corner(DL, buff=0.3)
        self.add(plano)
        self.play(Create(folium), Create(lemniscata), run_time=2)
        self.play(FadeIn(formulas))
        self.wait()
