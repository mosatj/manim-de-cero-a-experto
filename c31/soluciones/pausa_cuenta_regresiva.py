from manim import *


class CuentaRegresiva(Scene):
    def construct(self):
        pregunta = Text(
            "¿Cuánto suman los ángulos de un triángulo?",
            font_size=32,
        ).to_edge(UP)
        triangulo = Polygon(
            LEFT * 2 + DOWN,
            RIGHT * 2 + DOWN,
            UP * 1.5,
            color=BLUE,
            fill_opacity=0.4,
        )
        self.play(Write(pregunta), Create(triangulo))
        # Cuenta regresiva de 5 s: un número por segundo
        numero = Integer(5, font_size=96, color=YELLOW).to_corner(
            DR
        )
        self.add(numero)
        for n in range(4, -1, -1):
            self.wait(1)
            numero.set_value(n)
        respuesta = MathTex(
            r"\alpha+\beta+\gamma=180^\circ", font_size=56
        ).next_to(triangulo, DOWN)
        self.play(FadeOut(numero), Write(respuesta))
