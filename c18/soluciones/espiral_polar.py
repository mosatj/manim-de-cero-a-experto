from manim import *


class EspiralPolar(Scene):
    def construct(self):
        plano = PolarPlane(radius_max=3, size=7, azimuth_step=12,
                           background_line_style={
                               "stroke_opacity": 0.5})
        plano.add_coordinates()
        # Espiral de Arquímedes: el radio crece igual que el ángulo
        # theta hasta 12 rad (casi dos vueltas): r llega a 3
        espiral = plano.plot_polar_graph(lambda th: 0.25 * th,
                                         [0, 12], color=YELLOW)
        formula = MathTex(r"r=\tfrac{1}{4}\,\theta").to_corner(UL)
        self.add(plano, formula)
        self.play(Create(espiral), run_time=3, rate_func=linear)
        self.wait()
