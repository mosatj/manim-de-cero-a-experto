from manim import *

f = lambda t, y: y - t**2 + 1
exacta = lambda t: (t + 1)**2 - 0.5 * np.exp(t)


def poligonal_euler(ejes, h, color):
    t, y, puntos = 0.0, 0.5, [ejes.c2p(0, 0.5)]
    for _ in range(round(2 / h)):
        t, y = t + h, y + h * f(t, y)
        puntos.append(ejes.c2p(t, y))
    return VMobject(color=color).set_points_as_corners(puntos)


class EulerRefinado(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 2.2, 0.5], y_range=[0, 6, 1],
                    x_length=9, y_length=6, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 24}).to_edge(LEFT)
        curva = ejes.plot(exacta, x_range=[0, 2], color=BLUE)
        self.add(ejes, curva)
        actual = poligonal_euler(ejes, 0.5, YELLOW)
        rotulo = MathTex("h = 0.5").to_corner(UR)
        self.play(Create(actual), Write(rotulo))
        for h, color in ((0.25, ORANGE), (0.125, RED)):
            nueva = poligonal_euler(ejes, h, color)
            self.play(ReplacementTransform(actual, nueva),
                      Transform(rotulo, MathTex(f"h = {h}")
                                .to_corner(UR)))
            actual = nueva
