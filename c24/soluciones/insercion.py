import sys
from pathlib import Path
from manim import *

# El módulo arreglo_barras.py está en la carpeta superior
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from arreglo_barras import ArregloBarras  # noqa: E402


def insercion_eventos(lista):
    a = list(lista)
    for i in range(1, len(a)):
        j = i
        yield "toma", i, None
        # desplaza hacia atrás
        while j > 0 and a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
            yield "intercambia", j - 1, j
            j -= 1
        # 0..i ya ordenado
        yield "suelta", j, i


class Insercion(Scene):
    def construct(self):
        valores = [5, 2, 8, 1, 9, 3, 7, 4]
        arreglo = ArregloBarras(valores)
        self.add(arreglo)
        for tipo, i, j in insercion_eventos(valores):
            if tipo == "toma":
                self.play(arreglo.colorear([i], YELLOW),
                          run_time=0.3)
            elif tipo == "intercambia":
                self.play(arreglo.intercambiar(i, j), run_time=0.4)
            else:
                self.play(arreglo.colorear(range(j + 1), GREEN_C),
                          run_time=0.3)
        self.wait()
