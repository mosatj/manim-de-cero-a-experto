from manim import *


def guias(margen=0.6):
    """Tercios y zona segura: ayuda de maquetación, no de escena."""
    ancho, alto = config.frame_width, config.frame_height
    segura = Rectangle(width=ancho - 2 * margen,
                       height=alto - 2 * margen)
    segura.set_stroke(RED, width=2, opacity=0.8)
    lineas = VGroup(*[
        DashedLine([x, -alto / 2, 0], [x, alto / 2, 0])
        for x in (-ancho / 6, ancho / 6)
    ], *[
        DashedLine([-ancho / 2, y, 0], [ancho / 2, y, 0])
        for y in (-alto / 6, alto / 6)
    ]).set_stroke(GREY_C, width=1.5, opacity=0.7)
    return VGroup(segura, lineas)


class RejillaComposicion(Scene):
    def construct(self):
        ancho, alto = config.frame_width, config.frame_height
        titulo = Text("Circunferencia unitaria", font_size=40)
        titulo.to_corner(UL, buff=0.9)
        circulo = Circle(radius=1.8, color=BLUE)
        circulo.move_to([-ancho / 6, -0.4, 0])  # en un punto fuerte
        punto = Dot(circulo.point_at_angle(PI / 3), color=YELLOW)
        radio = Line(circulo.get_center(), punto.get_center(),
                     color=YELLOW)
        formula = MathTex(r"\cos^2\theta+\sin^2\theta=1", font_size=52)
        formula.move_to([ancho / 6 + 0.8, alto / 6 - 1.2, 0])
        self.add(guias())  # quítala antes del render final
        self.play(FadeIn(titulo), Create(circulo), Create(radio),
                  FadeIn(punto), Write(formula))
