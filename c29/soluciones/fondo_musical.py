import sys
import wave
from pathlib import Path

import numpy as np
from manim import *

sys.path.append(str(Path(__file__).parent.parent))
from sonido_basico import crear_tono


def crear_acorde(ruta, duracion=4.0, muestras=22050):
    """Un acorde suave (la, do#, mi) que sirve de fondo."""
    t = np.arange(int(duracion * muestras)) / muestras
    notas = (220, 277.2, 329.6)
    senal = sum(np.sin(2 * np.pi * f * t) for f in notas)
    senal *= np.minimum(1, np.minimum(t, duracion - t) / 0.5) / 3
    with wave.open(str(ruta), "wb") as archivo:
        archivo.setnchannels(1)
        archivo.setsampwidth(2)
        archivo.setframerate(muestras)
        datos = (0.6 * senal * 32767).astype(np.int16)
        archivo.writeframes(datos.tobytes())


class FondoMusical(Scene):
    def construct(self):
        carpeta = Path(config.media_dir)
        crear_acorde(carpeta / "fondo.wav")
        crear_tono(carpeta / "clic.wav")
        # El fondo, muy bajo (-15 dB)
        self.add_sound(str(carpeta / "fondo.wav"), gain=-15)
        puntos = VGroup(*[Dot() for _ in range(3)]).arrange(RIGHT)
        for punto in puntos:
            self.add_sound(str(carpeta / "clic.wav"))  # encima
            self.play(FadeIn(punto, scale=3), run_time=1)
        self.wait()
