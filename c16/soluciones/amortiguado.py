from manim import *

W, GAMMA, H = 2.0, 0.2, 0.1   # pulsación, freno, paso (grande)


def exacta(t):     # x'' = -W² x - 2 GAMMA x', x(0) = 1, v(0) = 0
    wd = np.sqrt(W**2 - GAMMA**2)
    fase = np.cos(wd * t) + GAMMA / wd * np.sin(wd * t)
    return np.exp(-GAMMA * t) * fase


def euler(semi, T=10):
    x, v, puntos = 1.0, 0.0, [(0, 1.0)]
    for k in range(round(T / H)):
        a = -W**2 * x - 2 * GAMMA * v
        if semi:
            v = v + H * a
            x = x + H * v
        else:
            x, v = x + H * v, v + H * a
        puntos.append(((k + 1) * H, x))
    return puntos


class Amortiguado(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 10, 1], y_range=[-2, 2, 1],
                    x_length=11, y_length=5.5, tips=False)
        curvas = VGroup(ejes.plot(exacta, x_range=[0, 10]))
        for semi, color in [(False, RED), (True, GREEN)]:
            curvas.add(VMobject(color=color).set_points_as_corners(
                [ejes.c2p(t, x) for t, x in euler(semi)]))
        leyenda = VGroup(Text("exacta"),
                         Text("Euler explícito", color=RED),
                         Text("semi-implícito", color=GREEN))
        leyenda.scale(0.5).arrange(RIGHT, buff=0.6).to_edge(UP)
        self.add(ejes, leyenda)
        self.play(Create(curvas, lag_ratio=0), run_time=3,
                  rate_func=linear)
