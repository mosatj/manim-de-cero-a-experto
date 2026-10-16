from manim import *


def plano_a():
    """Último fotograma del clip A: la tangente en x = -2."""
    ejes = Axes(x_range=[-3, 3], y_range=[-2, 3], x_length=9,
                y_length=6, tips=False)
    curva = ejes.plot(lambda x: 0.5 * x**2 - 2, color=BLUE_D)
    tangente = ejes.plot(lambda x: -2 * (x + 2), x_range=[-3, -1],
                         color=RED_D)
    punto = Dot(ejes.c2p(-2, 0), radius=0.15, color=RED_D)
    return VGroup(ejes, curva, tangente, punto)


FOCO_A = plano_a()[-1].get_center()  # foco del ojo al final de A


def panel(foco_b, titulo):
    """A en gris, B encima y el salto del ojo entre ambos focos."""
    marco = Rectangle(width=14.2, height=8, color=GRAY)
    formula = MathTex(r"f'(-2) = -2", font_size=96, color=RED_D)
    formula.move_to(foco_b).add_background_rectangle(opacity=1)
    salto = np.linalg.norm(foco_b - FOCO_A)
    flecha = Arrow(FOCO_A, formula.get_corner(DL), stroke_width=10,
                   color=GRAY_D) if salto > 2 else VGroup()
    ojo = Circle(radius=0.7, color=GRAY_D, stroke_width=8)
    fantasma = plano_a().set_stroke(opacity=0.3)  # A, ya saliendo
    fantasma[-1].set_fill(opacity=0.3)
    grupo = VGroup(marco, fantasma, ojo.move_to(FOCO_A), flecha,
                   formula)
    grupo.scale(0.44)
    rotulo = Text(titulo, font_size=32).next_to(grupo, UP)
    medida = Text(f"salto: {salto:.1f} unidades".replace(".", ","),
                  font_size=28).next_to(grupo, DOWN)
    return VGroup(rotulo, grupo, medida)


class RecorridoOjo(Scene):
    def construct(self):
        mal = panel(np.array([3.6, 2.4, 0]), "El ojo debe buscar")
        bien = panel(FOCO_A + 1.6 * UP, "El ojo ya está allí")
        VGroup(mal, bien).arrange(RIGHT, buff=0.5)
        self.play(FadeIn(mal), FadeIn(bien))
        self.wait()
