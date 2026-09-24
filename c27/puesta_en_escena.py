from manim import *


def diagrama():
    formula = MathTex("A", "=", r"\frac{1}{2}", "b", "h",
                      font_size=72)
    triangulo = Polygon([-2, -1, 0], [2, -1, 0], [0.8, 1.6, 0],
                        color=BLUE)
    altura = DashedLine([0.8, 1.6, 0], [0.8, -1, 0], color=YELLOW)
    base = Line([-2, -1, 0], [2, -1, 0], color=ORANGE)
    figura = VGroup(triangulo, altura, base).shift(3 * LEFT)
    formula.shift(3 * RIGHT)
    return figura, formula


class PuestaAntes(Scene):
    def construct(self):
        figura, formula = diagrama()
        extra = VGroup(
            Text("Triángulo", font_size=30).to_corner(UL),
            Text("Fórmula del área", font_size=30).to_corner(UR),
            Text("Unidades: cm²", font_size=26).to_corner(DR),
        )
        self.add(figura, formula, extra)
        # Todo a la vez y con la misma fuerza visual: ¿adónde miro?
        self.play(*[Indicate(m) for m in [*figura, *formula]])


class PuestaDespues(Scene):
    def construct(self):
        figura, formula = diagrama()
        self.add(figura, formula)
        # Foco único: la altura y su símbolo; el resto se atenúa
        foco = VGroup(figura[1], formula[4])
        resto = VGroup(figura[0], figura[2], *formula[:4])
        self.play(resto.animate.fade(0.65),
                  formula[4].animate.set_color(YELLOW))
        self.play(Indicate(foco, color=YELLOW, scale_factor=1.15))
