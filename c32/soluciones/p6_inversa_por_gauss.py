import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent  # codigo/c32
sys.path.insert(0, str(RAIZ / "proyecto6"))
from manim import *
from eliminacion import gauss_jordan
from escena_gauss import GaussJordan
from estilo import SOLUCION, TEXTO
from vista_matriz import MatrizAmpliada

# Determinante 1: la inversa tiene entradas enteras
A = [[1, 2, 1], [1, 3, 2], [1, 1, 1]]
IDENTIDAD = [[int(i == j) for j in range(3)] for i in range(3)]


class InversaPorGauss(GaussJordan, Scene):  # Scene: así la
    # reconoce el renderizador del libro, que mira las bases
    ampliada = [fila + unidad for fila, unidad in zip(A, IDENTIDAD)]
    columnas = 3  # a la derecha de la barra hay tres columnas

    def construct(self):
        # Sin sistema de ecuaciones: la matriz [A | I] va centrada
        rotulo = MathTex(r"[A \mid I] \rightarrow [I \mid A^{-1}]",
                         font_size=44, color=TEXTO)
        rotulo.to_edge(UP, buff=0.3)
        self.vista = MatrizAmpliada(self.ampliada, self.columnas)
        self.vista.shift(0.4 * UP)
        self.narracion = Text(" ", font_size=26)
        self.play(Write(rotulo), FadeIn(self.vista))
        for evento in gauss_jordan(self.ampliada, self.columnas):
            self.animar_evento(evento)
        self.wait(2)

    def terminar(self, reducida):
        inversa = self.vista.matriz.get_columns()[self.columnas:]
        self.play(
            self.vista.quitar_marco(),
            self.vista.actualizar(reducida, None),
            FadeOut(self.vista.rotulo),
            self.narrar("A la derecha de la barra, la inversa"),
            run_time=0.8,
        )
        marco = SurroundingRectangle(inversa, color=SOLUCION,
                                     buff=0.15)
        self.play(Create(marco))
