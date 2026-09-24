import sys
from pathlib import Path

from manim import *

# Importa los componentes del proyecto desde su carpeta raíz
sys.path.append(str(Path(__file__).parent.parent / "proyecto"))
from componentes import CuadradoImpares, LeccionScene


class EtiquetaCapas(LeccionScene):
    titulo = "Cada capa, un impar"

    def construct(self):
        cuadro = CuadradoImpares(5).shift(0.3 * DOWN)
        self.add(cuadro)
        for k in range(1, 6):
            # La celda de la esquina de la L, arriba a la derecha
            esquina = cuadro.capa(k)[-1]
            numero = Integer(2 * k - 1, font_size=30)
            numero.next_to(esquina, UR, buff=0.05)
            self.play(Indicate(cuadro.capa(k)), FadeIn(numero),
                      run_time=0.6)
