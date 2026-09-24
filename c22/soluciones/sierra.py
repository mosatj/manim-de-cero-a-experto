from manim import *


def sierra(x, N):
    """Suma parcial de x = 2 * suma (-1)^(n+1) sen(nx)/n."""
    n = np.arange(1, N + 1)
    return 2 * np.sum((-1) ** (n + 1) * np.sin(np.outer(x, n)) / n,
                      axis=1)


class Sierra(Scene):
    def construct(self):
        ejes = Axes(x_range=[-3 * PI, 3 * PI, PI],
                    y_range=[-4, 4, 1], x_length=12, y_length=6,
                    tips=False)
        # Tres copias del diente: f(x) = x en (-pi, pi), periódica
        dientes = VGroup(*[
            ejes.plot(lambda x, c=c: x - c, color=GRAY,
                      x_range=[c - PI, c + PI - 0.01])
            for c in (-TAU, 0, TAU)])
        curva = ejes.plot(lambda x: sierra(np.array([x]), 15)[0],
                          x_range=[-3 * PI, 3 * PI, 0.005],
                          color=YELLOW)
        self.add(ejes, dientes)
        self.play(Create(curva), run_time=3)
        self.add(MathTex("N = 15", color=YELLOW).to_corner(UR))
