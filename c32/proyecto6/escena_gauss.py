from manim import *
from eliminacion import gauss_jordan, operacion
from estilo import SOLUCION, TAM_NARRACION, TAM_TITULO, TEXTO
from sistema import AMPLIADA, COLUMNAS_A, INCOGNITAS
from vista_matriz import MatrizAmpliada, sistema_latex


class GaussJordan(Scene):
    """Controlador: recorre los eventos del modelo y los traduce
    a animaciones de la vista. Cambiar el sistema no toca esta
    clase: una subclase redefine los atributos de clase."""

    ampliada = AMPLIADA
    columnas = COLUMNAS_A
    incognitas = INCOGNITAS
    titulo = "Gauss-Jordan sobre la matriz ampliada"

    def construct(self):
        rotulo = Text(self.titulo, font_size=TAM_TITULO,
                      color=TEXTO)
        rotulo.to_edge(UP, buff=0.3)
        self.sistema = MathTex(
            sistema_latex(self.ampliada, self.incognitas),
            font_size=40, color=TEXTO,
        ).move_to(3.6 * LEFT + 0.6 * UP)
        self.vista = MatrizAmpliada(self.ampliada, self.columnas)
        self.vista.move_to(2.4 * RIGHT + 0.4 * UP)
        self.narracion = Text(" ", font_size=TAM_NARRACION)
        self.play(Write(rotulo), Write(self.sistema))
        self.play(
            TransformFromCopy(self.sistema, self.vista.matriz),
            FadeIn(self.vista.barra),
        )
        self.wait(0.5)
        for evento in gauss_jordan(self.ampliada, self.columnas):
            self.animar_evento(evento)
        self.wait(2)

    def narrar(self, texto):
        nueva = Text(texto, font_size=TAM_NARRACION, color=TEXTO)
        return Transform(self.narracion, nueva.to_edge(DOWN))

    def animar_evento(self, evento):
        tipo, i = evento[0], evento[1]
        if tipo == "pivote":
            j = evento[2]
            self.play(
                self.vista.resaltar_pivote(i, j),
                self.narrar(f"Pivote: fila {i + 1}, "
                            f"columna {j + 1}"),
                run_time=0.8,
            )
        elif tipo in ("escalar", "eliminar", "intercambiar"):
            frases = {
                "escalar": f"Hacemos 1 el pivote "
                           f"de la fila {i + 1}",
                "eliminar": f"Anulamos la columna del pivote "
                            f"en la fila {i + 1}",
                "intercambiar": f"Intercambiamos las filas {i + 1} "
                                f"y {evento[2] + 1}",
            }
            self.play(
                self.vista.rotular(operacion(evento)),
                self.narrar(frases[tipo]),
                run_time=0.8,
            )
            self.play(self.vista.actualizar(evento[-1], i),
                      run_time=1.2)
            self.wait(0.4)
        elif tipo == "fin":
            self.terminar(evento[1])

    def terminar(self, reducida):
        solucion = VGroup(*[
            MathTex(f"{v} = {fila[-1]}", font_size=40,
                    color=SOLUCION)
            for v, fila in zip(self.incognitas, reducida)
        ]).arrange(RIGHT, buff=0.6)
        solucion.next_to(self.sistema, DOWN, buff=0.9)
        self.play(
            self.vista.quitar_marco(),
            self.vista.actualizar(reducida, None),  # sin fila azul
            FadeOut(self.vista.rotulo),
            self.narrar("La matriz reducida ya es la solución"),
            run_time=0.8,
        )
        self.play(Write(solucion))
