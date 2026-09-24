from manim import *


class Reloj(Scene):
    def construct(self):
        esfera = Circle(radius=3, color=GRAY_B)
        marcas, numeros = VGroup(), VGroup()
        for h in range(12):
            # Ángulo desde las 12, en sentido horario
            angulo = -h * TAU / 12
            larga = h % 3 == 0
            inicio = 2.6 * UP if larga else 2.75 * UP
            marca = Line(inicio, 2.95 * UP,
                         stroke_width=6 if larga else 3)
            marcas.add(marca.rotate(angulo, about_point=ORIGIN))
            numero = Text(str(h or 12), font_size=36)
            numero.move_to(rotate_vector(2.2 * UP, angulo))
            numeros.add(numero)
        # Manecillas a las 10:10, giradas desde las 12
        horaria = Line(ORIGIN, 1.4 * UP, stroke_width=10)
        minutero = Line(ORIGIN, 2.3 * UP, stroke_width=6)
        minutero.set_color(BLUE)
        horaria.rotate(-(10 + 10 / 60) * TAU / 12,
                       about_point=ORIGIN)
        minutero.rotate(-10 * TAU / 60, about_point=ORIGIN)
        self.add(esfera, marcas, numeros, horaria, minutero,
                 Dot(radius=0.12, color=RED))
