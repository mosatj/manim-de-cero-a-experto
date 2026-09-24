import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import *
from componentes import Reloj


class DosRelojes(Scene):
    def construct(self):
        # Dos instancias del mismo componente, independientes
        lima = Reloj(radio=1.8, horas=9, minutos=0)
        madrid = Reloj(radio=1.8, color=BLUE_B, horas=15, minutos=0)
        relojes = VGroup(lima, madrid).arrange(RIGHT, buff=2)
        nombres = VGroup(Text("Lima", font_size=32),
                         Text("Madrid", font_size=32))
        for n, r in zip(nombres, relojes):
            n.next_to(r, DOWN)
        self.add(relojes, nombres)
        # 90 minutos más tarde en ambas ciudades, a la vez
        self.play(lima.animar_hora(10, 30),
                  madrid.animar_hora(16, 30),
                  run_time=3)
