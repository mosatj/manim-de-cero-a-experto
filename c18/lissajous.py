from manim import *


class Lissajous(Scene):
    def construct(self):
        rango = [-1.2, 1.2, 0.5]
        ejes = Axes(x_range=rango, y_range=rango, x_length=6.5,
                    y_length=6.5, tips=False)
        # plot_parametric_curve recibe t -> (x(t), y(t))
        curva = ejes.plot_parametric_curve(
            lambda t: np.array([np.sin(3 * t), np.sin(4 * t)]),
            t_range=[0, TAU, 0.01])
        curva.set_color_by_gradient(TEAL, BLUE, PURPLE, YELLOW)
        lapiz = Dot(curva.get_start(), color=WHITE)
        formula = MathTex(r"x=\sin 3t", r"\\ y=\sin 4t",
                          font_size=40)
        formula.to_corner(UL)
        self.add(ejes, formula)
        # El punto recorre la curva mientras esta se dibuja
        self.play(Create(curva), MoveAlongPath(lapiz, curva),
                  run_time=5, rate_func=linear)
        self.wait()
