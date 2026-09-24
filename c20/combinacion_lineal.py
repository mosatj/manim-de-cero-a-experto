from manim import *


class CombinacionLineal(Scene):
    def construct(self):
        plano = NumberPlane(x_range=[-4, 6, 1], y_range=[-2, 5, 1],
                            x_length=10, y_length=7).to_edge(LEFT)
        v, w = np.array([2, 1]), np.array([-1, 2])
        a, b = ValueTracker(0.5), ValueTracker(0.5)
        punto = lambda x: plano.c2p(*x)
        # a·v y b·w con sus paralelas forman el paralelogramo
        av = always_redraw(lambda: Arrow(
            punto((0, 0)), punto(a.get_value() * v), buff=0,
            color=YELLOW))
        bw = always_redraw(lambda: Arrow(
            punto((0, 0)), punto(b.get_value() * w), buff=0,
            color=BLUE))
        comb = lambda: a.get_value() * v + b.get_value() * w
        lados = always_redraw(lambda: VGroup(
            DashedLine(punto(a.get_value() * v), punto(comb())),
            DashedLine(punto(b.get_value() * w), punto(comb()))))
        resultado = always_redraw(lambda: Arrow(
            punto((0, 0)), punto(comb()), buff=0, color=GREEN))

        v_a = DecimalNumber(0.5).add_updater(
            lambda m: m.set_value(a.get_value()))
        v_b = DecimalNumber(0.5).add_updater(
            lambda m: m.set_value(b.get_value()))
        panel = VGroup(
            MathTex(r"\vec v=(2,1)", color=YELLOW),
            MathTex(r"\vec w=(-1,2)", color=BLUE),
            VGroup(MathTex("a=", color=YELLOW), v_a).arrange(RIGHT),
            VGroup(MathTex("b=", color=BLUE), v_b).arrange(RIGHT),
            MathTex(r"a\vec v+b\vec w", color=GREEN))
        panel.arrange(DOWN, aligned_edge=LEFT)
        panel.to_edge(RIGHT, buff=0.4)
        meta = Dot(punto((3, 4)), color=RED)
        nom_meta = MathTex("(3,4)", color=RED)
        nom_meta.next_to(meta, UR, buff=0.1)

        self.add(plano, av, bw, lados, resultado, panel)
        self.play(FadeIn(meta), Write(nom_meta))
        self.play(a.animate.set_value(2), run_time=2)
        self.play(b.animate.set_value(1), run_time=2)
