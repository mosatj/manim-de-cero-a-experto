from manim import *


def ecuaciones():
    antes = MathTex("x", "+", "3", "=", "7", font_size=80).shift(UP)
    despues = MathTex("x", "=", "7", "-", "3", font_size=80).shift(UP)
    return antes, despues


def congelar(animacion, alfa):
    """El mobject de una animación detenida en el instante alfa."""
    animacion.begin()
    animacion.interpolate(alfa)
    return animacion.mobject


class TransicionAntes(Scene):
    def construct(self):
        antes, despues = ecuaciones()
        # Transform empareja curvas por orden, no por significado
        self.add(congelar(Transform(antes, despues), 0.5))
        self.add(Text("Transform, a mitad de camino", font_size=32,
                      color=GREY_B).to_edge(DOWN, buff=1.2))


class TransicionDespues(Scene):
    def construct(self):
        antes, despues = ecuaciones()
        # TransformMatchingTex empareja por subcadena: cada símbolo
        # viaja a su nuevo sitio y conserva su identidad
        animacion = TransformMatchingTex(antes, despues,
                                         path_arc=PI / 2)
        self.add(congelar(animacion, 0.5))
        rotulo = Text("TransformMatchingTex, a mitad de camino",
                      font_size=32, color=GREY_B)
        self.add(rotulo.to_edge(DOWN, buff=1.2))
