import os

from manim import *
from manim_voiceover import VoiceoverScene

from servicio_ensayo import ServicioEnsayo


def elegir_servicio():
    """VOZ=ensayo (defecto), gtts o clon, desde la terminal."""
    voz = os.environ.get("VOZ", "ensayo")
    if voz == "gtts":  # Google Translate: necesita internet
        from manim_voiceover.services.gtts import GTTSService
        return GTTSService(lang="es", tld="com.mx")
    if voz == "clon":  # modelo local de clonación (pesado)
        from manim_voiceover_qwen3_tts import (
            Qwen3VoiceCloningService, VoiceProfile)
        perfil = VoiceProfile(
            name="autor", ref_audio="voz/muestra.wav",
            ref_text=open("voz/muestra.txt").read())
        return Qwen3VoiceCloningService(voices=[perfil],
                                        device="mps")
    return ServicioEnsayo()


class VozServicios(VoiceoverScene):
    def construct(self):
        servicio = elegir_servicio()
        self.set_speech_service(servicio)
        cuadrado = Square(3, color=BLUE, fill_opacity=0.3)
        with self.voiceover(text="Un cuadrado de lado tres.") as t:
            self.play(DrawBorderThenFill(cuadrado),
                      run_time=t.duration)
        nombre = type(servicio).__name__
        rotulo = Text(f"Servicio: {nombre}", font_size=32)
        self.add(rotulo.to_edge(DOWN))
