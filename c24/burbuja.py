from manim import *
from arreglo_barras import ArregloBarras   # módulo de esta carpeta


def burbuja_eventos(lista):
    a = list(lista)
    for fin in range(len(a) - 1, 0, -1):
        for j in range(fin):
            yield "compara", j, j + 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                yield "intercambia", j, j + 1
        yield "fija", fin, None       # el mayor ya está al final
    yield "fija", 0, None


class Burbuja(Scene):
    def construct(self):
        valores = [5, 2, 8, 1, 9, 3, 7, 4]
        arreglo = ArregloBarras(valores).shift(0.5 * DOWN)
        comparaciones, intercambios = Integer(0), Integer(0)
        marcador = VGroup(
            VGroup(Tex("comparaciones:"), comparaciones),
            VGroup(Tex("intercambios:"), intercambios))
        for par in marcador:
            par.arrange(RIGHT)
        marcador.arrange(RIGHT, buff=1).to_edge(UP)
        self.add(arreglo, marcador)
        for tipo, i, j in burbuja_eventos(valores):
            if tipo == "compara":
                comparaciones.increment_value()
                self.play(arreglo.colorear([i, j], YELLOW),
                          run_time=0.25)
                self.play(arreglo.colorear([i, j], BLUE_C),
                          run_time=0.1)
            elif tipo == "intercambia":
                intercambios.increment_value()
                self.play(arreglo.intercambiar(i, j), run_time=0.4)
            else:
                self.play(arreglo.colorear([i], GREEN_C),
                          run_time=0.2)
        self.wait()
