from manim import *
from impares import COLORES, escuadra, cuadrado_de_escuadras

# Las viñetas del storyboard: el fotograma clave de cada bloque del
# guion. Son funciones para poder reutilizarlas en el animatic.


def vineta(n):
    if n == 1:  # gancho
        suma = MathTex("1+3+5+7", "=", r"\text{?}", font_size=96)
        return suma.set_color_by_tex("?", YELLOW)
    if n == 2:  # pregunta
        cuadrados = VGroup(*[MathTex(str(k * k), font_size=80,
                                     color=COLORES[k - 1])
                             for k in range(1, 6)])
        return cuadrados.arrange(RIGHT, buff=0.9)
    if n == 3:  # construcción: escuadras separadas
        piezas = VGroup(*[escuadra(k, 0.55) for k in range(1, 5)])
        return piezas.arrange(RIGHT, buff=0.8, aligned_edge=DOWN)
    figura = cuadrado_de_escuadras(4, 0.55)  # generalización
    formula = MathTex(r"1+3+\cdots+(2n-1)=n^2", font_size=64)
    return VGroup(figura, formula.next_to(figura, DOWN, buff=0.7))


def ampliar(grupo):
    """Llena el cuadro: la viñeta se imprimirá pequeña."""
    return grupo.scale(min(11 / grupo.width, 6.5 / grupo.height))


class Vineta1(Scene):
    def construct(self):
        self.add(ampliar(vineta(1)))


class Vineta2(Scene):
    def construct(self):
        self.add(ampliar(vineta(2)))


class Vineta3(Scene):
    def construct(self):
        self.add(ampliar(vineta(3)))


class Vineta4(Scene):
    def construct(self):
        self.add(ampliar(vineta(4)))
