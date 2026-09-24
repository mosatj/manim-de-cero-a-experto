import sys
from pathlib import Path
from manim import *

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from arreglo_barras import ArregloBarras  # noqa: E402


class ArregloEditable(ArregloBarras):
    """Añade (por herencia) la operación a[k] = valor."""

    def asignar(self, k, valor, escala=0.45):
        columna = self.barras[k]
        barra, numero = columna
        nueva = barra.copy().stretch_to_fit_height(valor * escala)
        nueva.move_to(barra, aligned_edge=DOWN)
        texto = MathTex(str(valor), font_size=30).move_to(numero)
        self.valores[k] = valor
        return AnimationGroup(Transform(barra, nueva),
                              Transform(numero, texto))


def mezcla_eventos(a, izq, der):
    """Ordena a[izq:der] por mezcla; anuncia cada escritura."""
    if der - izq <= 1:
        return
    medio = (izq + der) // 2
    yield from mezcla_eventos(a, izq, medio)
    yield from mezcla_eventos(a, medio, der)
    izquierda, derecha = a[izq:medio], a[medio:der]   # copias
    i = j = 0
    yield "tramo", izq, der
    # toma el menor de las dos cabezas
    for k in range(izq, der):
        if j == len(derecha) or (i < len(izquierda)
                                 and izquierda[i] <= derecha[j]):
            a[k], i = izquierda[i], i + 1
        else:
            a[k], j = derecha[j], j + 1
        yield "escribe", k, a[k]


class Mezcla(Scene):
    def construct(self):
        valores = [5, 2, 8, 1, 9, 3, 7, 4]
        arreglo = ArregloEditable(valores)
        self.add(arreglo)
        n = len(valores)
        for tipo, i, j in mezcla_eventos(list(valores), 0, n):
            if tipo == "tramo":
                self.play(arreglo.colorear(range(n), BLUE_C),
                          arreglo.colorear(range(i, j), YELLOW),
                          run_time=0.3)
            else:
                self.play(arreglo.asignar(i, j), run_time=0.3)
        self.play(arreglo.colorear(range(len(valores)), GREEN_C))
        self.wait()
