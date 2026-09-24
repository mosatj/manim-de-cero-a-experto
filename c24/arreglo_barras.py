from manim import *


class ArregloBarras(VGroup):
    """Arreglo de números dibujado como barras con su valor debajo.

    Los métodos devuelven animaciones: la escena decide cuándo
    reproducirlas. self.barras sigue siempre el orden en pantalla.
    """

    def __init__(self, valores, ancho=0.8, escala=0.45, **kwargs):
        super().__init__(**kwargs)
        self.valores = list(valores)
        self.barras = []
        for k, v in enumerate(self.valores):
            barra = Rectangle(width=0.85 * ancho, height=v * escala,
                              fill_color=BLUE_C, fill_opacity=0.9,
                              stroke_width=1)
            barra.move_to([k * ancho, 0, 0], aligned_edge=DOWN)
            numero = MathTex(str(v), font_size=30)
            numero.next_to(barra, DOWN, buff=0.15)
            columna = VGroup(barra, numero)
            self.barras.append(columna)
            self.add(columna)
        self.center()

    def colorear(self, indices, color):
        return AnimationGroup(*[
            self.barras[k][0].animate.set_fill(color)
            for k in indices])

    def intercambiar(self, i, j):
        bi, bj = self.barras[i], self.barras[j]
        animacion = AnimationGroup(
            bi.animate(path_arc=-PI / 2).set_x(bj.get_x()),
            bj.animate(path_arc=-PI / 2).set_x(bi.get_x()),
        )
        # El estado cambia ya; la imagen, cuando se reproduzca
        self.barras[i], self.barras[j] = bj, bi
        v = self.valores
        v[i], v[j] = v[j], v[i]
        return animacion
