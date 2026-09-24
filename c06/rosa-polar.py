from manim import *


def rosa(k, radio=2.5):
    """Rosa polar r = radio·cos(kθ) como curva paramétrica."""
    return lambda th: radio * np.cos(k * th) * np.array(
        [np.cos(th), np.sin(th), 0])


def lissajous(a, b, radio=2.5):
    return lambda t: radio * np.array(
        [np.sin(a * t + PI / 2), np.sin(b * t), 0])


class RosaPolar(Scene):
    def construct(self):
        curva1 = ParametricFunction(rosa(4), t_range=[0, TAU],
                                    color=YELLOW)
        curva2 = ParametricFunction(lissajous(3, 4),
                                    t_range=[0, TAU], color=BLUE)
        VGroup(curva1, curva2).arrange(RIGHT, buff=1.2)
        rotulo1 = MathTex(r"r=\cos 4\theta").next_to(curva1, DOWN)
        rotulo2 = MathTex(r"(\cos 3t,\ \sin 4t)")
        rotulo2.next_to(curva2, DOWN)
        self.play(Create(curva1), Create(curva2), run_time=3)
        self.play(Write(rotulo1), Write(rotulo2))
