import sys
from pathlib import Path

from manim import *
from manim_voiceover import VoiceoverScene

sys.path.append(str(Path(__file__).parent.parent))
from servicio_ensayo import ServicioEnsayo


class ServicioEnsayoPausado(ServicioEnsayo):
    """Pausa larga tras . ? ! y corta tras , ; :"""

    def pausa(self, palabra):
        if palabra[-1] in ".?!":
            return 0.5
        if palabra[-1] in ",;:":
            return 0.2
        return 0.0


class EnsayoPausado(VoiceoverScene):
    def construct(self):
        self.set_speech_service(ServicioEnsayoPausado())
        texto = ("Primero, el guion. <bookmark mark='a'/>Después, "
                 "la animación.")
        with self.voiceover(text=texto) as t:
            self.wait_until_bookmark("a")
        marca = t.bookmark_times["a"] - t.start_t
        linea = f"a: {marca:.2f} s   total: {t.duration:.2f} s"
        self.add(Text(linea, font_size=36))
