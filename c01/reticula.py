from manim import *


def reticula(ancho, alto, columnas, filas, margen, calle):
    """Retícula modular: márgenes, columnas, filas y calles entre ellas.
    Devuelve el dibujo y una función que da el rectángulo de un bloque."""
    col = (ancho - 2 * margen - (columnas - 1) * calle) / columnas
    fil = (alto - 2 * margen - (filas - 1) * calle) / filas
    marco = Rectangle(width=ancho, height=alto, color=GREY_C,
                      stroke_width=3)
    modulos = VGroup(*[
        Rectangle(width=col, height=fil, stroke_width=0,
                  fill_color=TEAL_E, fill_opacity=0.07).move_to([
            -ancho / 2 + margen + col / 2 + i * (col + calle),
            alto / 2 - margen - fil / 2 - j * (fil + calle), 0])
        for i in range(columnas) for j in range(filas)])

    def bloque(c0, c1, f0, f1):
        """Rectángulo que ocupa de la columna c0 a c1 y de la fila f0 a f1
        (contando desde 1, de izquierda a derecha y de arriba abajo)."""
        x0 = -ancho / 2 + margen + (c0 - 1) * (col + calle)
        x1 = -ancho / 2 + margen + c1 * (col + calle) - calle
        y0 = alto / 2 - margen - (f0 - 1) * (fil + calle)
        y1 = alto / 2 - margen - f1 * (fil + calle) + calle
        return Rectangle(width=x1 - x0, height=y0 - y1).move_to(
            [(x0 + x1) / 2, (y0 + y1) / 2, 0])

    return VGroup(marco, modulos), bloque


def barras(lineas, ancho):
    """Un párrafo esquemático: barras grises en lugar de letras."""
    return VGroup(*[Rectangle(height=0.11, width=ancho * (0.6 if k == lineas
                                                          - 1 else 1),
                              stroke_width=0, fill_color=GREY_C,
                              fill_opacity=1)
                    for k in range(lineas)]).arrange(DOWN, buff=0.16,
                                                     aligned_edge=LEFT)


def contenido(bloque_titulo, bloque_figura, bloque_formula, bloque_texto,
              tam):
    titulo = Text("Teorema de Pitágoras", font_size=tam, weight=BOLD)
    titulo.scale_to_fit_width(min(titulo.width, bloque_titulo.width))
    titulo.align_to(bloque_titulo, UL)
    a, b = 3, 4
    triangulo = Polygon(ORIGIN, RIGHT * a, RIGHT * a + UP * b,
                        color=BLUE, fill_opacity=0.5)
    cuadrados = VGroup(
        Square(a).next_to(triangulo, DOWN, buff=0).align_to(triangulo,
                                                            LEFT),
        Square(b).next_to(triangulo, RIGHT, buff=0).align_to(triangulo,
                                                             DOWN),
        # el de la hipotenusa, hacia afuera (normal (-b, a))
        Polygon(ORIGIN, [a, b, 0], [a - b, b + a, 0], [-b, a, 0]),
    ).set_stroke(GREY_B, 3)
    figura = VGroup(triangulo, cuadrados)
    figura.scale_to_fit_height(bloque_figura.height * 0.95)
    figura.scale_to_fit_width(min(figura.width, bloque_figura.width))
    figura.move_to(bloque_figura)
    formula = MathTex("a^2+b^2=c^2", font_size=tam * 1.3)
    formula.scale_to_fit_width(min(formula.width, bloque_formula.width))
    formula.move_to(bloque_formula).align_to(bloque_formula, LEFT)
    texto = barras(4, bloque_texto.width).align_to(bloque_texto, UL)
    return VGroup(titulo, figura, formula, texto)


class Reticula(Scene):
    def construct(self):
        # 16:9 con 12 columnas y 6 filas (las medidas del marco de Manim)
        horizontal, b = reticula(14.22, 8, 12, 6, 0.6, 0.2)
        h_contenido = contenido(b(1, 12, 1, 1), b(1, 6, 2, 6),
                                b(7, 12, 2, 2), b(7, 11, 3, 5), 48)
        # 9:16 con 4 columnas y 8 filas: la misma jerarquía, apilada
        vertical, v = reticula(8, 14.22, 4, 8, 0.6, 0.2)
        v_contenido = contenido(v(1, 4, 1, 1), v(1, 4, 2, 4),
                                v(1, 4, 5, 5), v(1, 4, 6, 7), 48)
        h = VGroup(horizontal, h_contenido).scale(0.6)
        vv = VGroup(vertical, v_contenido).scale(0.46)
        VGroup(h, vv).arrange(RIGHT, buff=0.6, aligned_edge=UP)
        rotulos = VGroup(
            Text("16:9 · 12 columnas × 6 filas", font_size=26)
            .next_to(h, DOWN, buff=0.25),
            Text("9:16 · 4 columnas", font_size=26)
            .next_to(vv, DOWN, buff=0.25))
        VGroup(h, vv, rotulos).move_to(ORIGIN)
        self.add(h, vv, rotulos)
