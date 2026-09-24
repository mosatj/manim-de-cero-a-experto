import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent  # codigo/c32
sys.path.insert(0, str(RAIZ / "proyecto1"))
from manim import *
from componentes import MarcoPitagoras, rotulo


class PitagorasIsosceles(Scene):
    """Con a = b los dos huecos de la derecha son iguales."""

    def construct(self):
        izquierda = MarcoPitagoras(a=1.6, b=1.6).move_to(LEFT * 3.4)
        derecha = MarcoPitagoras(a=1.6, b=1.6).move_to(RIGHT * 3.4)
        derecha.triangulos.become(derecha.destinos(2))
        hueco, huecos = izquierda.hueco_c(), derecha.huecos_ab()
        self.add(izquierda, derecha)
        self.play(FadeIn(hueco), FadeIn(huecos))
        self.play(
            Write(rotulo("c^2", hueco)),
            Write(rotulo("a^2", huecos[0])),
            Write(rotulo("a^2", huecos[1])),
        )
