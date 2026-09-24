from manim import *


def logistica(r, x0, n):
    """Órbita x0, x1, ..., xn de x_{k+1} = r x_k (1 - x_k)."""
    x = [x0]
    for _ in range(n):
        x.append(r * x[-1] * (1 - x[-1]))
    return x


class SerieLogistica(Scene):
    def construct(self):
        n = 40
        ejes = Axes(x_range=[0, n, 5], y_range=[0, 1, 0.2],
                    x_length=11, y_length=5.5, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 22}).to_edge(DOWN)
        rotulo = Variable(2.5, "r").to_corner(UL)
        r = rotulo.tracker            # el ValueTracker de Variable
        serie = always_redraw(lambda: VMobject(
            color=RED, stroke_width=5).set_points_as_corners(
            [ejes.c2p(k, x) for k, x in
             enumerate(logistica(r.get_value(), 0.2, n))]))
        formula = MathTex(r"x_{n+1} = r\,x_n(1 - x_n),\ x_0 = 0.2",
                          font_size=34).to_corner(UR)
        self.add(ejes, serie, rotulo, formula)
        # punto fijo -> ciclo 2 -> ciclo 4 -> caos
        for valor in (2.8, 3.2, 3.5, 3.9):
            self.play(r.animate.set_value(valor), run_time=3,
                      rate_func=linear)
