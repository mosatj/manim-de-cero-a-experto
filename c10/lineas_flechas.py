from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class LineasYFlechas(Scene):
    def construct(self):
        # 1) Line entre dos objetos: va de borde a borde
        a = Circle(0.5, color=BLUE)
        b = Square(1, color=BLUE).shift(3 * RIGHT)
        p1 = VGroup(a, b, Line(a, b, color=YELLOW))
        # 2) buff (hueco en los extremos) y path_arc (curvatura)
        c = Line(LEFT, RIGHT, buff=0.3)
        d = Line(LEFT, RIGHT, path_arc=PI / 2, color=GREEN)
        p2 = VGroup(Dot(LEFT), Dot(RIGHT), c,
                    d.shift(0.6 * DOWN))
        # 3) Arrow deja buff=0.25 por defecto en cada extremo
        e, f = Dot(), Dot(3 * RIGHT)
        p3 = VGroup(e, f, Arrow(e, f, color=RED))
        # 4) Vector: flecha que parte del origen
        plano = NumberPlane(x_range=(-1, 3), y_range=(-1, 2),
                            x_length=4, y_length=3)
        v = Vector([2, 1], color=YELLOW).shift(plano.c2p(0, 0))
        p4 = VGroup(plano, v)
        rotulos = ["Line(a, b)", "buff=0.3 / path_arc=PI/2",
                   "Arrow(e, f)", "Vector([2, 1])"]
        paneles = VGroup()
        for panel, t in zip([p1, p2, p3, p4], rotulos):
            texto = Text(t, font_size=26).next_to(panel, DOWN)
            paneles.add(VGroup(panel, texto))
        paneles.arrange_in_grid(rows=2, cols=2, buff=(1.5, 1))
        self.add(paneles)
