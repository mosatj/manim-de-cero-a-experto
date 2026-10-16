"""¿Cuánto cuesta regenerar con Asymptote? Se mide con una caché
vacía (en frío) y otra vez con la caché llena."""
import tempfile
import time

import numpy as np
from asy_fotogramas import fotograma

valores = np.linspace(0, 1, 9)
with tempfile.TemporaryDirectory() as cache:
    for vuelta in ["en frío", "con caché"]:
        inicio = time.perf_counter()
        for t in valores:
            fotograma("asy_euler_movil.asy", t, cache=cache)
        ms = (time.perf_counter() - inicio) / len(valores) * 1000
        print(f"{vuelta:>9}: {ms:7.1f} ms por fotograma")
        if vuelta == "en frío":
            frio = ms
# Regenerar CADA fotograma de 4 s de vídeo a 30 fps
print(f"120 fotogramas en frío: unos {120 * frio / 1000:.0f} s")
