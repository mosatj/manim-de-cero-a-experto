from manim import *


def triangulo():
    return Polygon([-2, -1.5, 0], [2, -1.5, 0], [-2, 1.5, 0])


class ContiguidadAntes(Scene):
    def construct(self):
        t = triangulo().shift(3 * LEFT)
        numeros = VGroup(
            Text("1", font_size=30).next_to(t, DOWN),
            Text("2", font_size=30).next_to(t, LEFT),
            Text("3", font_size=30).move_to(t.get_center() + 0.6 * UR),
        )
        leyenda = VGroup(
            Text("1: cateto a", font_size=28),
            Text("2: cateto b", font_size=28),
            Text("3: hipotenusa c", font_size=28),
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(DR)
        self.play(Create(t), FadeIn(numeros), FadeIn(leyenda))


class ContiguidadDespues(Scene):
    def construct(self):
        t = triangulo().shift(3 * LEFT)
        a = MathTex("a").next_to(t, DOWN)
        b = MathTex("b").next_to(t, LEFT)
        c = MathTex("c", color=YELLOW)
        c.move_to(t.get_center() + 0.6 * UR)
        nota = Text("hipotenusa: frente\nal ángulo recto",
                    font_size=24, color=YELLOW)
        nota.next_to(c, RIGHT, buff=0.4)
        formula = MathTex("a^2+b^2=", "c", "^2")
        formula.shift(3.5 * RIGHT + DOWN)
        formula[1].set_color(YELLOW)
        self.play(Create(t), Write(VGroup(a, b, c)))
        self.play(FadeIn(nota), Write(formula))
