import sys
from pathlib import Path
from manim import *

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from arreglo_barras import ArregloBarras  # noqa: E402


class Seleccion(Scene):
    def construct(self):
        valores = [5, 2, 8, 1, 9, 3, 7, 4]
        arreglo = ArregloBarras(valores)
        self.add(arreglo)
        a = list(valores)
        for i in range(len(a)):
            minimo = i
            self.play(arreglo.colorear([i], RED_C), run_time=0.2)
            for j in range(i + 1, len(a)):
                self.play(arreglo.colorear([j], YELLOW),
                          run_time=0.15)
                if a[j] < a[minimo]:
                    if minimo != i:
                        azul = arreglo.colorear([minimo], BLUE_C)
                        self.play(azul, run_time=0.1)
                    minimo = j
                    self.play(arreglo.colorear([j], RED_C),
                              run_time=0.15)
                else:
                    self.play(arreglo.colorear([j], BLUE_C),
                              run_time=0.1)
            if minimo != i:
                a[i], a[minimo] = a[minimo], a[i]
                self.play(arreglo.intercambiar(i, minimo),
                          run_time=0.4)
            self.play(arreglo.colorear([i], GREEN_C), run_time=0.2)
        self.wait()
