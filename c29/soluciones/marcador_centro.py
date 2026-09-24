import sys
from pathlib import Path

from manim import *
from manim_voiceover import VoiceoverScene

sys.path.append(str(Path(__file__).parent.parent))
from servicio_ensayo import ServicioEnsayo


class MarcadorCentro(VoiceoverScene):
    def construct(self):
        self.set_speech_service(ServicioEnsayo())
        circulo = Circle(radius=2.5, color=BLUE)
        centro = Dot(color=YELLOW)
        with self.voiceover(
            text="Toda circunferencia tiene un <bookmark mark='c'/>"
                 "centro que equidista de sus puntos."
        ) as t:
            hasta_c = t.time_until_bookmark("c")
            self.play(Create(circulo), run_time=hasta_c)
            self.play(GrowFromCenter(centro), run_time=0.4)
        self.add(MathTex("O").next_to(centro, DR, buff=0.1))
