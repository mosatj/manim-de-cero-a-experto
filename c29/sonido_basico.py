import wave
from pathlib import Path

import numpy as np
from manim import *


def crear_tono(ruta, frecuencia=660, duracion=0.12, muestras=22050):
    """Escribe un .wav corto: un «clic» con caída exponencial."""
    t = np.arange(int(duracion * muestras)) / muestras
    senal = np.sin(2 * np.pi * frecuencia * t) * np.exp(-30 * t)
    datos = (0.5 * senal * 32767).astype(np.int16)  # 16 bits
    with wave.open(str(ruta), "wb") as archivo:
        archivo.setnchannels(1)
        archivo.setsampwidth(2)
        archivo.setframerate(muestras)
        archivo.writeframes(datos.tobytes())


class SonidoBasico(Scene):
    def construct(self):
        clic = Path(config.media_dir) / "clic.wav"
        crear_tono(clic)
        puntos = VGroup(*[Dot(radius=0.25) for _ in range(4)])
        puntos.arrange(RIGHT, buff=1.2)
        self.add(puntos)
        for punto in puntos:
            self.add_sound(str(clic))  # suena en este instante
            instante = Text(f"{self.time:.1f} s", font_size=28)
            self.add(instante.next_to(punto, DOWN, buff=0.5))
            self.play(punto.animate.set_color(BLUE).scale(1.6),
                      run_time=0.5)
        # Otro clic, más agudo, 0,25 s más tarde
        crear_tono(Path(config.media_dir) / "agudo.wav", 1320)
        self.add_sound(str(Path(config.media_dir) / "agudo.wav"),
                       time_offset=0.25, gain=-6)
        self.play(Circumscribe(puntos, color=YELLOW))
