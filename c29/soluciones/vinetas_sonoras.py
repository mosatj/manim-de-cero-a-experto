import sys
from pathlib import Path

from manim import *

# La carpeta del capítulo, para importar sonido_basico
sys.path.append(str(Path(__file__).parent.parent))
from sonido_basico import crear_tono


class VinetasSonoras(Scene):
    def construct(self):
        clic = Path(config.media_dir) / "clic.wav"
        crear_tono(clic, frecuencia=880)
        lista = BulletedList("Guion", "Boceto", "Código", "Voz",
                             font_size=44)
        for vineta in lista:
            self.add_sound(str(clic))
            self.play(FadeIn(vineta, shift=RIGHT), run_time=0.6)
            self.wait(0.3)
