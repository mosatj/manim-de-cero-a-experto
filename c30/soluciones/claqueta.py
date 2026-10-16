import wave
from pathlib import Path

import numpy as np
from manim import *


def pip(ruta, duracion, frecuencia=1000, muestras=48000):
    """Escribe un tono de 1 kHz que dura exactamente `duracion`."""
    t = np.arange(round(duracion * muestras)) / muestras
    datos = (0.6 * np.sin(2 * np.pi * frecuencia * t) * 32767)
    with wave.open(str(ruta), "wb") as archivo:
        archivo.setnchannels(1)
        archivo.setsampwidth(2)
        archivo.setframerate(muestras)
        archivo.writeframes(datos.astype(np.int16).tobytes())


class Claqueta(Scene):
    """Cuenta atrás con un «pip» dos segundos antes del inicio."""

    def construct(self):
        un_fotograma = 1 / config.frame_rate
        ruta = Path(config.media_dir) / "pip.wav"
        ruta.parent.mkdir(parents=True, exist_ok=True)
        pip(ruta, un_fotograma)
        anillo = Circle(radius=2.2, color=GREY_B, stroke_width=6)
        tres = Text("3", font_size=160)
        self.add(anillo, tres)
        self.wait(1)
        # Un solo fotograma: destello blanco, «2» y pip a la vez
        destello = FullScreenRectangle(fill_color=WHITE,
                                       fill_opacity=1)
        dos = Text("2", font_size=160, color=BLACK)
        self.remove(tres)
        self.add(destello, dos)
        self.add_sound(str(ruta))
        self.wait(un_fotograma)
        self.remove(destello, dos, anillo)
        self.wait(2 - un_fotograma)  # negro hasta el programa
        inicio = Text(f"t = {self.time:.2f} s: empieza la lección",
                      font_size=40)
        self.add(inicio)
        self.wait(1)
