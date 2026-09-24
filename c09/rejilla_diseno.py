from manim import *


def rejilla_de_tercios(color=GRAY, opacidad=0.6):
    """Líneas que dividen el marco en tercios."""
    ancho, alto = config.frame_width, config.frame_height
    lineas = VGroup()
    for k in (-1, 1):
        x, y = k * ancho / 6, k * alto / 6
        lineas.add(DashedLine([x, -alto / 2, 0],
                              [x, alto / 2, 0]))
        lineas.add(DashedLine([-ancho / 2, y, 0],
                              [ancho / 2, y, 0]))
    return lineas.set_stroke(color, 2, opacidad)


class RejillaDiseno(Scene):
    def construct(self):
        guia = NumberPlane(
            background_line_style={"stroke_opacity": 0.2},
            axis_config={"stroke_opacity": 0.3})
        titulo = Text("El área del círculo", font_size=46)
        titulo.to_edge(UP)
        circulo = Circle(1.7, color=BLUE, fill_opacity=0.3)
        radio = Line(circulo.get_center(), circulo.get_right(),
                     color=YELLOW)
        r = MathTex("r", color=YELLOW).next_to(radio, UP, 0.1)
        figura = VGroup(circulo, radio, r)
        tercio = config.frame_width / 6
        figura.move_to([-tercio, -0.5, 0])
        formula = MathTex(r"A = \pi r^2", font_size=80)
        formula.move_to([tercio, -0.5, 0])
        # Ayudas primero (quedan debajo); fuera en el render final
        self.add(guia, rejilla_de_tercios())
        self.add(titulo, figura, formula)
