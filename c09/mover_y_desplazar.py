from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class MoverYDesplazar(Scene):
    def construct(self):
        tenue = {"stroke_opacity": 0.3}
        self.add(NumberPlane(background_line_style=tenue))
        punto = np.array([3, 2, 0])
        self.add(Dot(punto, color=YELLOW),
                 MathTex("(3,2)").next_to(punto, RIGHT, buff=0.7))
        # Dos cuadrados que parten del mismo lugar
        a = Square(1.2, color=BLUE, fill_opacity=0.5)
        b = Square(1.2, color=RED, fill_opacity=0.5)
        VGroup(a, b).move_to([-3, -1, 0])
        fantasma = DashedVMobject(a.copy().set_fill(opacity=0))
        inicio = a.get_center()
        # move_to: posición ABSOLUTA (el centro va al punto)
        a.move_to(punto)
        # shift: desplazamiento RELATIVO (se suma el vector)
        b.shift(punto)
        self.add(fantasma, a, b,
                 Arrow(inicio, a.get_center(), color=BLUE),
                 Arrow(inicio, b.get_center(), color=RED))
        t1 = Text("a.move_to([3, 2, 0])", font_size=30, color=BLUE)
        t2 = Text("b.shift([3, 2, 0])", font_size=30, color=RED)
        codigo = VGroup(t1, t2).arrange(DOWN, aligned_edge=LEFT)
        codigo.to_corner(UL)
        self.add(BackgroundRectangle(codigo), codigo)
