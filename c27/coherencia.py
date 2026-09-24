from manim import *


def circulo_con_radio():
    circulo = Circle(radius=1.6, color=BLUE)
    radio = Line(ORIGIN, 1.6 * RIGHT, color=YELLOW)
    r = MathTex("r", color=YELLOW).next_to(radio, UP, buff=0.1)
    return VGroup(circulo, radio, r)


class CoherenciaAntes(Scene):
    def construct(self):
        self.add(NumberPlane())  # cuadrícula que no aporta nada
        estrellas = VGroup(*[
            Star(outer_radius=0.15, color=random_bright_color(),
                 fill_opacity=1).move_to([x, y, 0])
            for x, y in [(-6, 3), (5.5, 2.5), (-5, -3), (6, -3), (3, 3)]
        ])
        titulo = Text("¡¡EL ÁREA DEL CÍRCULO!!", weight=BOLD)
        titulo.set_color_by_gradient(RED, YELLOW, GREEN, PURPLE)
        titulo.to_edge(UP)
        lema = Text("¡La matemática es divertida!", font_size=26,
                    color=PINK).to_corner(DL)
        figura = circulo_con_radio().shift(2.5 * LEFT + 0.3 * DOWN)
        formula = MathTex(r"A=\pi r^2", font_size=60, color=GREEN)
        formula.shift(2.5 * RIGHT)
        self.add(estrellas, titulo, lema)
        self.play(SpinInFromNothing(figura), Write(formula))


class CoherenciaDespues(Scene):
    def construct(self):
        figura = circulo_con_radio().shift(2.5 * LEFT)
        formula = MathTex(r"A=\pi", "r", "^2", font_size=60)
        formula[1].set_color(YELLOW)  # la misma r que en la figura
        formula.shift(2.5 * RIGHT)
        self.play(Create(figura[:2]), Write(figura[2]))
        self.play(Write(formula))
