# Renderiza la misma escena de 2 s en varios formatos y compara
import subprocess
import sys
import tempfile
from pathlib import Path

import av

PRUEBAS = [("mp4", []), ("webm", ["--format", "webm"]),
           ("gif", ["--format", "gif"]),
           ("mov", ["--format", "mov"]), ("mp4 -t", ["-t"]),
           ("webm -t", ["-t", "--format", "webm"]),
           ("png-seq", ["--format", "png-sequence"])]

print(f"{'orden':9}{'archivo':8}{'códec':7}{'píxeles':9}alfa KB")
for nombre, extra in PRUEBAS:
    with tempfile.TemporaryDirectory() as carpeta:
        orden = [sys.executable, "-m", "manim", "-ql", *extra,
                 "--media_dir", carpeta, "muestra_formatos.py",
                 "MuestraFormatos"]
        subprocess.run(orden, check=True, capture_output=True)
        salidas = [p for p in Path(carpeta, "videos").rglob("*.*")
                   if p.is_file() and "partial" not in str(p)]
        if nombre == "png-seq":
            salidas = list(Path(carpeta, "images").rglob("*.png"))
        kb = sum(p.stat().st_size for p in salidas) / 1024
        with av.open(str(salidas[0])) as c:
            flujo = c.streams.video[0]
            codec = flujo.codec_context.name
            pix = flujo.codec_context.pix_fmt
            # ¿Transparencia? VP9 la guarda aparte (alpha_mode)
            rgba = next(c.decode(flujo)).to_ndarray(format="rgba")
            alfa = (flujo.metadata.get("alpha_mode") == "1"
                    or rgba[..., 3].min() < 255)
    tipo = salidas[0].suffix
    if nombre == "png-seq":
        tipo = f"{len(salidas)} png"
    print(f"{nombre:9}{tipo:8}{codec:7}{pix:9}"
          f"{'sí' if alfa else 'no':5}{kb:.0f}")
