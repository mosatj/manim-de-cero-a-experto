# Ejercicio 32.14: la misma escena base del proyecto 1 (GuionScene, con el
# método decir), pero narrada con manim-voiceover. Las escenas no cambian:
# siguen llamando a self.decir(clave, ...). Ver p1_demostracion_con_voz.py.
import sys
from pathlib import Path
from textwrap import fill

RAIZ = Path(__file__).resolve().parent.parent.parent  # codigo/
sys.path.insert(0, str(RAIZ / "c32" / "proyecto1"))
sys.path.append(str(RAIZ / "c29"))
from manim import *  # antes que manim_voiceover
from manim.animation.animation import prepare_animation
from manim_voiceover import VoiceoverScene
from servicio_ensayo import ServicioEnsayo
from estilo import FONDO, TEXTO, TAM_SUBTITULO
from guion import texto


class GuionScene(VoiceoverScene):
    """Escena base con voz: cada frase dura lo que dura su audio."""

    def setup(self):
        super().setup()
        self.camera.background_color = FONDO
        self.subtitulo = VMobject()
        # Servicio de ensayo (sin red, capítulo 29). Para la voz definitiva:
        #   from manim_voiceover.services.gtts import GTTSService
        #   self.set_speech_service(GTTSService(lang="es"))
        # o un servicio de voz clonada como manim-voiceover-qwen3-tts.
        self.set_speech_service(ServicioEnsayo())

    def decir(self, clave, *animaciones):
        nuevo = Text(
            fill(texto(clave), 55),
            font_size=TAM_SUBTITULO,
            color=TEXTO,
            line_spacing=0.8,
        )
        nuevo.to_edge(DOWN, buff=0.3)
        with self.voiceover(text=texto(clave)) as tracker:
            cambio = [
                FadeOut(self.subtitulo, run_time=0.3),
                FadeIn(nuevo, run_time=0.3),
            ]
            # La duración ya no sale de duracion(clave), sino del audio
            animaciones = [
                prepare_animation(a).set_run_time(tracker.duration)
                for a in animaciones
            ]
            self.play(*cambio, *animaciones)
            # Al salir del bloque, voiceover espera a que termine la frase
        self.subtitulo = nuevo
