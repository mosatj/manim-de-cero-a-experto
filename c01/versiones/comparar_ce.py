from manim import *  # Manim Community


class Comparacion(Scene):
    def construct(self):
        titulo = Text("Una escena, dos versiones", font_size=40)
        self.play(Write(titulo.to_edge(UP)))
        circulo = Circle(radius=1, color=BLUE).shift(LEFT * 4)
        cuadrado = Square(2, color=GREEN).shift(LEFT * 4)
        self.play(Create(circulo))              # crear un trazo
        self.play(Transform(circulo, cuadrado))
        formula = MathTex(r"f(x) = x^2")        # fórmula: MathTex
        self.play(Write(formula.to_corner(UR)))
        ejes = Axes(x_range=[-2, 2], y_range=[0, 4],
                    x_length=5, y_length=3.5).shift(RIGHT * 2)
        curva = ejes.plot(lambda x: x**2, color=YELLOW)  # .plot
        self.play(Create(ejes), Create(curva))
        x = ValueTracker(-2)
        punto = always_redraw(
            lambda: Dot(ejes.c2p(x.get_value(), x.get_value()**2)))
        self.add(punto)
        self.play(x.animate.set_value(2), run_time=3)
        self.wait()
