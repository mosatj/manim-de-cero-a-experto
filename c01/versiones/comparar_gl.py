from manimlib import *  # ManimGL, la versión de Grant Sanderson


class Comparacion(Scene):
    def construct(self):
        titulo = Text("Una escena, dos versiones", font_size=40)
        self.play(Write(titulo.to_edge(UP)))
        circulo = Circle(radius=1, color=BLUE).shift(LEFT * 4)
        cuadrado = Square(2, color=GREEN).shift(LEFT * 4)
        self.play(ShowCreation(circulo))        # crear un trazo
        self.play(Transform(circulo, cuadrado))
        formula = Tex(r"f(x) = x^2")            # fórmula: Tex
        self.play(Write(formula.to_corner(UR)))
        ejes = Axes(x_range=[-2, 2], y_range=[0, 4],
                    width=5, height=3.5).shift(RIGHT * 2)
        curva = ejes.get_graph(lambda x: x**2,  # .get_graph
                               color=YELLOW)
        self.play(ShowCreation(ejes), ShowCreation(curva))
        x = ValueTracker(-2)
        punto = always_redraw(
            lambda: Dot(ejes.c2p(x.get_value(), x.get_value()**2)))
        self.add(punto)
        self.play(x.animate.set_value(2), run_time=3)
        self.wait()
