from manim import *


class DeterminanteArea(Scene):
    def construct(self):
        plano = NumberPlane(x_range=[-2, 5], y_range=[-2, 4],
                            x_length=8.4, y_length=7.2)
        plano.to_edge(LEFT)
        A = np.array([[1, 2], [2, 1]])            # det A = −3
        t = ValueTracker(0)
        # M(t) = (1 − t) I + t A  va de la identidad a A
        M = lambda: (1 - t.get_value())*np.eye(2) + t.get_value()*A
        det = lambda: np.linalg.det(M())
        pt = lambda x, y: plano.c2p(x, y)

        def paralelogramo():
            (a, b), (c, d) = M()          # columnas (a, c) y (b, d)
            color = BLUE if det() >= 0 else RED
            return Polygon(pt(0, 0), pt(a, c), pt(a + b, c + d),
                           pt(b, d), color=color, fill_opacity=0.5)

        def base():
            (a, b), (c, d) = M()
            o = pt(0, 0)
            return VGroup(Arrow(o, pt(a, c), buff=0, color=GREEN),
                          Arrow(o, pt(b, d), buff=0, color=YELLOW))

        figura = always_redraw(paralelogramo)
        flechas = always_redraw(base)
        v_t = DecimalNumber(0).add_updater(
            lambda m: m.set_value(t.get_value()))
        v_d = DecimalNumber(1, include_sign=True).add_updater(
            lambda m: m.set_value(det()))
        panel = VGroup(
            MathTex(r"M(t)=(1-t)I+tA"),
            MathTex(r"A=\begin{bmatrix}1&2\\2&1\end{bmatrix}"),
            VGroup(MathTex("t="), v_t).arrange(RIGHT),
            VGroup(MathTex(r"\det M(t)="), v_d).arrange(RIGHT),
            MathTex(r"=1-4t^2"))
        panel.arrange(DOWN, aligned_edge=LEFT)
        panel.to_edge(RIGHT, buff=0.3)

        self.add(plano, figura, flechas, panel)
        self.play(t.animate.set_value(0.35), run_time=2)
        self.play(t.animate.set_value(0.5), run_time=1.5)
        self.play(t.animate.set_value(0.75), run_time=1.5)
        self.play(t.animate.set_value(1), run_time=1.5)
