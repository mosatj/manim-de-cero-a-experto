from manim import *


class Rosas56(Scene):
    def construct(self):
        paneles = VGroup()
        for k in (5, 6):
            ejes = Axes(x_range=[-1.2, 1.2], y_range=[-1.2, 1.2],
                        x_length=5, y_length=5, tips=False,
                        axis_config={"include_ticks": False,
                                     "stroke_opacity": 0.4})
            rosa = ejes.plot_polar_graph(
                lambda t, k=k: np.cos(k * t), [0, TAU],
                color=YELLOW, stroke_width=4)
            petalos = k if k % 2 else 2 * k     # regla de las rosas
            titulo = MathTex(rf"r=\cos {k}\theta:\ {petalos}"
                             r"\ \text{pétalos}", font_size=36)
            titulo.next_to(ejes, UP)
            paneles.add(VGroup(ejes, rosa, titulo))
        paneles.arrange(RIGHT, buff=1)
        self.play(Create(paneles), run_time=3)
