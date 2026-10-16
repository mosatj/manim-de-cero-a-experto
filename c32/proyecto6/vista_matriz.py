from manim import *
from eliminacion import como_latex
from estilo import CAMBIO, GRIS, PIVOTE, SOLUCION, TAM_ROTULO, TEXTO


def sistema_latex(ampliada, incognitas):
    """El sistema de ecuaciones de [A | b] como texto de LaTeX."""
    filas = []
    for fila in ampliada:
        terminos = ""
        for a, v in zip(fila, incognitas):
            if a == 0:
                continue
            signo = "-" if a < 0 else ("+" if terminos else "")
            coef = "" if abs(a) == 1 else str(abs(a))
            terminos += f"{signo}{coef}{v}"
        filas.append(rf"{terminos} &= {fila[-1]}")
    cuerpo = r" \\ ".join(filas)
    return r"\begin{cases}" + cuerpo + r"\end{cases}"


class MatrizAmpliada(VGroup):
    """Vista: la matriz ampliada [A | B] con su barra, un marco
    para el pivote y un rótulo con la operación. Sus métodos no
    animan: devuelven animaciones para self.play()."""

    def __init__(self, filas, columnas, **kwargs):
        super().__init__(**kwargs)
        self.columnas = columnas
        self.matriz = self._construir(filas)
        self.barra = self._barra(self.matriz)
        self.marco = VMobject()  # aún no hay pivote
        self.rotulo = MathTex("")
        self.rotulo.next_to(self.matriz, DOWN, buff=0.6)
        self.add(self.matriz, self.barra, self.marco, self.rotulo)

    def _construir(self, filas, cambiada=None):
        """Una Matrix de Manim a partir de las fracciones del
        modelo; la fila `cambiada` se pinta de otro color."""
        textos = [[como_latex(x) for x in fila] for fila in filas]
        matriz = Matrix(textos, h_buff=1.1, v_buff=0.9)
        matriz.set_color(TEXTO)
        for fila in matriz.get_rows():
            fila[self.columnas :].set_color(SOLUCION)
        if cambiada is not None:
            matriz.get_rows()[cambiada].set_color(CAMBIO)
        return matriz

    def _barra(self, matriz):
        columnas = matriz.get_columns()
        izquierda = columnas[self.columnas - 1].get_right()
        derecha = columnas[self.columnas].get_left()
        x = (izquierda[0] + derecha[0]) / 2
        corchete = matriz.get_brackets()[0]
        return DashedLine(
            [x, corchete.get_bottom()[1], 0],
            [x, corchete.get_top()[1], 0],
            color=GRIS,
            stroke_width=2,
        )

    # --- Una animación por cada evento del algoritmo ---
    def resaltar_pivote(self, i, j):
        entrada = self.matriz.get_rows()[i][j]
        nuevo = SurroundingRectangle(entrada, color=PIVOTE,
                                     buff=0.12)
        anterior, self.marco = self.marco, nuevo
        self.remove(anterior).add(nuevo)
        if anterior.has_points():
            return ReplacementTransform(anterior, nuevo)
        return Create(nuevo)

    def rotular(self, latex):
        nuevo = MathTex(latex, font_size=TAM_ROTULO, color=PIVOTE)
        nuevo.next_to(self.matriz, DOWN, buff=0.6)
        return Transform(self.rotulo, nuevo)

    def actualizar(self, filas, cambiada):
        """Sustituye la matriz por la nueva: las entradas se
        transforman una a una porque ambas tienen la misma forma."""
        nueva = self._construir(filas, cambiada)
        nueva.move_to(self.matriz)
        return Transform(self.matriz, nueva)

    def quitar_marco(self):
        anterior, self.marco = self.marco, VMobject()
        self.remove(anterior).add(self.marco)
        return FadeOut(anterior)
