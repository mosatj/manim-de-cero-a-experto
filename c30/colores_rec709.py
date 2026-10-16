# ¿Qué colores verá un editor que lea el vídeo como Rec. 709?
import subprocess
import sys
import tempfile
from pathlib import Path

import av

from carta_color import PALETA


def centros(rgb):
    """Píxel central de cada muestra (marco de 1280 x 720)."""
    return [tuple(int(v) for v in rgb[293, 192 + 306 * i])
            for i in range(len(PALETA))]


def renderizar(carpeta):
    subprocess.run([sys.executable, "-m", "manim", "-qm",
                    "--format", "mp4",
                    "--media_dir", carpeta, "carta_color.py",
                    "CartaColor"], check=True, capture_output=True)
    return next(Path(carpeta).rglob("CartaColor.mp4"))


def leer(video, matriz=None):
    with av.open(str(video)) as contenedor:
        flujo = contenedor.streams.video[0]
        etiqueta = flujo.codec_context.colorspace
        cuadro = next(contenedor.decode(flujo))
        rgb = cuadro.reformat(format="rgb24",
                              src_colorspace=matriz).to_ndarray()
    return etiqueta, centros(rgb)


MATRICES = {1: "bt709", 2: "sin especificar", 6: "smpte170m"}
esperado = [tuple(int(h[k:k + 2], 16) for k in (1, 3, 5))
            for h in PALETA]
with tempfile.TemporaryDirectory() as carpeta:
    video = renderizar(carpeta)
    etiqueta, como601 = leer(video, "itu601")
    _, como709 = leer(video, "itu709")
print(f"{'color':9}{'original':16}{'leído 601':16}leído 709")
for h, a, b, c in zip(PALETA, esperado, como601, como709):
    print(f"{h:9}{str(a):16}{str(b):16}{c}")
print("Matriz declarada en el archivo:", MATRICES[etiqueta])
