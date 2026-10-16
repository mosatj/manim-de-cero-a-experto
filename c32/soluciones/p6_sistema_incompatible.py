import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent  # codigo/c32
sys.path.insert(0, str(RAIZ / "proyecto6"))
from manim import *
from escena_gauss import GaussJordan
from estilo import SOLUCION

# Las dos primeras ecuaciones son incompatibles: x + y + z vale
# 4 en una y 2x + 2y + 2z vale 10 (es decir, x + y + z = 5) en otra
INCOMPATIBLE = [
    [1, 1, 1, 4],
    [2, 2, 2, 10],
    [1, 2, 3, 7],
]


class SistemaIncompatible(GaussJordan, Scene):  # Scene: así la
    # reconoce el renderizador del libro, que mira las bases
    ampliada = INCOMPATIBLE
    titulo = "Un sistema sin solución"

    def animar_evento(self, evento):
        if evento[0] == "incompatible":
            self.fila_mala = evento[1]  # se usa en terminar()
        else:
            super().animar_evento(evento)

    def terminar(self, reducida):
        self.play(self.vista.quitar_marco(),
                  self.vista.actualizar(reducida, None),
                  FadeOut(self.vista.rotulo), run_time=0.8)
        fila = self.vista.matriz.get_rows()[self.fila_mala]
        aviso = Text("Sistema incompatible", font_size=40,
                     color=SOLUCION)
        aviso.next_to(self.sistema, DOWN, buff=0.9)
        self.play(
            fila.animate.set_color(SOLUCION),
            self.narrar("Una fila dice 0 = c con c distinto de 0"),
            run_time=0.8,
        )
        self.play(Write(aviso))
