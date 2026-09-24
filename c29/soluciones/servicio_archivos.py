import sys
from pathlib import Path

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.base import SpeechService

sys.path.append(str(Path(__file__).parent.parent))
from sonido_basico import crear_tono


class ServicioArchivos(SpeechService):
    """Usa grabaciones previas: un archivo por frase del guion."""

    def __init__(self, grabaciones, **kwargs):
        self.grabaciones = grabaciones  # {texto: ruta del .wav}
        super().__init__(**kwargs)

    def generate_from_text(self, text, cache_dir=None, path=None,
                           **kwargs):
        ruta = Path(self.grabaciones[text]).resolve()
        # Las rutas se guardan relativas a la carpeta de caché
        cache = Path(self.cache_dir).resolve()
        return {"input_text": text,
                "original_audio": str(ruta.relative_to(cache))}


class ConGrabaciones(VoiceoverScene):
    def construct(self):
        carpeta = Path(config.media_dir) / "voiceovers"
        carpeta.mkdir(parents=True, exist_ok=True)
        # En un proyecto real serían tus grabaciones de Audacity
        crear_tono(carpeta / "f1.wav", duracion=1.5)
        crear_tono(carpeta / "f2.wav", duracion=2.0)
        frase1 = "Un triángulo."
        frase2 = "Y su circunferencia inscrita."
        frases = {frase1: carpeta / "f1.wav",
                  frase2: carpeta / "f2.wav"}
        self.set_speech_service(ServicioArchivos(frases))
        tri = Triangle(color=BLUE).scale(2)
        with self.voiceover(text=frase1) as t:
            self.play(Create(tri), run_time=t.duration)
        with self.voiceover(text=frase2) as t:
            circ = Circle(radius=1, color=YELLOW).move_to(tri)
            self.play(Create(circ), run_time=t.duration)
        rotulo = Text(f"{t.duration:.1f} s", font_size=30)
        self.add(rotulo.to_edge(DOWN))
