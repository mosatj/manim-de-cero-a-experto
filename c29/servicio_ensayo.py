"""Servicio de voz de ensayo para manim-voiceover, sin red.

Genera un .wav con un pulso suave por palabra (una duración
realista para el texto) y anota dónde empieza cada palabra: así
los marcadores <bookmark mark="..."/> funcionan como con una voz.
Sirve para ajustar el ritmo antes de sintetizar la voz definitiva.
"""
import wave
from pathlib import Path

import manim  # noqa: F401  (antes que manim_voiceover)
import numpy as np
from manim_voiceover.helper import remove_bookmarks
from manim_voiceover.services.base import SpeechService

MUESTRAS = 22050        # muestras de audio por segundo
UNIDAD = 10_000_000     # manim-voiceover mide en 1e-7 s


class ServicioEnsayo(SpeechService):
    """Servicio propio: basta con escribir generate_from_text."""

    def __init__(self, segundos_por_palabra=0.36, **kwargs):
        self.segundos_por_palabra = segundos_por_palabra
        super().__init__(**kwargs)

    def generate_from_text(self, text, cache_dir=None, path=None,
                           **kwargs):
        carpeta = Path(cache_dir or self.cache_dir)
        limpio = remove_bookmarks(text)
        entrada = {"input_text": limpio,
                   "service": type(self).__name__,
                   "config": {"spp": self.segundos_por_palabra}}
        # Si ya se generó este mismo texto, se reutiliza (caché)
        previo = self.get_cached_result(entrada, carpeta)
        if previo is not None:
            return previo
        nombre = path or self.get_audio_basename(entrada) + ".wav"
        fronteras = self._escribir_wav(carpeta / nombre, limpio)
        return {"input_text": text, "input_data": entrada,
                "original_audio": str(nombre),
                "word_boundaries": fronteras}

    def _escribir_wav(self, ruta, texto):
        paso = self.segundos_por_palabra
        trozos, fronteras, t, desde = [], [], 0.0, 0
        for palabra in texto.split():
            posicion = texto.index(palabra, desde)
            desde = posicion + len(palabra)
            fronteras.append({"audio_offset": int(t * UNIDAD),
                              "text_offset": posicion,
                              "word_length": len(palabra),
                              "text": palabra,
                              "boundary_type": "Word"})
            dur = paso + self.pausa(palabra)
            trozos.append(self._pulso(dur))
            t += dur
        fronteras.append({"audio_offset": int(t * UNIDAD),
                          "text_offset": len(texto),
                          "word_length": 0, "text": "",
                          "boundary_type": "Word"})
        senal = np.concatenate(trozos) if trozos else np.zeros(1)
        muestras = (senal * 32767).astype(np.int16)
        with wave.open(str(ruta), "wb") as archivo:
            archivo.setnchannels(1)
            archivo.setsampwidth(2)
            archivo.setframerate(MUESTRAS)
            archivo.writeframes(muestras.tobytes())
        return fronteras

    def pausa(self, palabra):
        """Silencio extra tras la puntuación, como al hablar."""
        return 0.25 if palabra[-1] in ".,;:?!" else 0.0

    def _pulso(self, duracion):
        n = int(duracion * MUESTRAS)
        tiempo = np.arange(n) / MUESTRAS
        sonando = int(0.6 * self.segundos_por_palabra * MUESTRAS)
        envolvente = np.zeros(n)
        envolvente[:sonando] = np.hanning(sonando)
        tono = np.sin(2 * np.pi * 180 * tiempo) + 0.3 * np.sin(
            2 * np.pi * 360 * tiempo)
        return 0.2 * envolvente * tono

