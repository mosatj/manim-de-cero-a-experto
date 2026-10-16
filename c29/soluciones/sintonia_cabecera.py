import sys
import wave
from pathlib import Path

import numpy as np
from manim import *

sys.path.append(str(Path(__file__).parent.parent))
from sonido_basico import crear_tono


def crear_acorde(ruta, duracion=2.0, muestras=22050):
    """Un acorde breve (la, do#, mi) para la cabecera."""
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


class SintoniaCabecera(Scene):
    def construct(self):
        carpeta = Path(config.media_dir)
        crear_acorde(carpeta / "sintonia.wav")
        crear_tono(carpeta / "clic.wav")
        # Cabecera: la sintonía dura lo mismo que el título (2 s)
        self.add_sound(str(carpeta / "sintonia.wav"), gain=-6)
        titulo = Text("Tres puntos", font_size=56)
        self.play(Write(titulo), run_time=1.5)
        self.play(titulo.animate.scale(0.6).to_edge(UP),
                  run_time=0.5)
        # Explicación: sin música debajo; solo un clic por punto
        puntos = VGroup(*[Dot() for _ in range(3)]).arrange(RIGHT)
        for punto in puntos:
            self.add_sound(str(carpeta / "clic.wav"))
            self.play(FadeIn(punto, scale=3), run_time=1)
        self.wait()
