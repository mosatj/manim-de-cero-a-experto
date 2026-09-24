from manim import *
from arreglo_barras import ArregloBarras


def quicksort_eventos(a, bajo, alto):
    """Quicksort con partición de Lomuto; ordena la lista a."""
    if bajo > alto:
        return
    if bajo == alto:
        yield "fija", bajo, None
        return
    yield "rango", bajo, alto
    pivote = a[alto]
    yield "pivote", alto, None
    i = bajo                          # frontera de los menores
    for j in range(bajo, alto):
        yield "compara", j, alto
        if a[j] < pivote:
            if i != j:
                a[i], a[j] = a[j], a[i]
                yield "intercambia", i, j
            i += 1
    if i != alto:
        a[i], a[alto] = a[alto], a[i]
        yield "intercambia", i, alto
    yield "fija", i, None      # el pivote ya está en su sitio
    yield from quicksort_eventos(a, bajo, i - 1)
    yield from quicksort_eventos(a, i + 1, alto)


class Quicksort(Scene):
    def construct(self):
        valores = [6, 3, 9, 1, 8, 2, 7, 4, 5]
        arreglo = ArregloBarras(valores).shift(0.5 * DOWN)
        titulo = Tex("Quicksort (partición de Lomuto)").to_edge(UP)
        self.add(arreglo, titulo)
        fijos = set()
        barras = arreglo.barras
        eventos = quicksort_eventos(list(valores), 0, 8)
        for tipo, i, j in eventos:
            if tipo == "rango":   # atenúa lo que no se toca ahora
                self.play(*[b.animate.set_opacity(
                    1 if i <= k <= j or k in fijos else 0.25)
                    for k, b in enumerate(barras)], run_time=0.3)
            elif tipo == "pivote":
                self.play(arreglo.colorear([i], RED_C),
                          run_time=0.3)
            elif tipo == "compara":
                self.play(arreglo.colorear([i], YELLOW),
                          run_time=0.2)
                self.play(arreglo.colorear([i], BLUE_C),
                          run_time=0.1)
            elif tipo == "intercambia":
                self.play(arreglo.intercambiar(i, j), run_time=0.4)
            else:
                fijos.add(i)
                self.play(arreglo.colorear([i], GREEN_C),
                          run_time=0.2)
        self.play(*[b.animate.set_opacity(1) for b in barras])
        self.wait()
