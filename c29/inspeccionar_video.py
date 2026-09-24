# Renderiza una escena con voz y examina el vídeo resultante
import subprocess
import sys
import tempfile
from pathlib import Path

import av  # PyAV: la biblioteca con la que Manim codifica

with tempfile.TemporaryDirectory() as carpeta:
    subprocess.run([sys.executable, "-m", "manim", "-ql",
                    "--media_dir", carpeta, "voz_primera.py",
                    "VozPrimera"],
                   check=True, capture_output=True)
    video = next(Path(carpeta).rglob("VozPrimera.mp4"))
    with av.open(str(video)) as contenedor:
        print("Contenedor:", contenedor.format.name)
        print(f"Duración: {contenedor.duration / 1e6:.2f} s")
        for flujo in contenedor.streams:
            ctx = flujo.codec_context
            if flujo.type == "video":
                fps = float(flujo.average_rate)
                tam = f"{ctx.width}x{ctx.height}"
                print(f"Vídeo: {ctx.name}, {tam}, {fps:g} fps")
            else:
                print(f"Audio: {ctx.name}, {ctx.sample_rate} Hz")
    print("--- subtítulos (.srt) ---")
    srt = video.with_suffix(".srt").read_text(encoding="utf-8")
    print(srt.strip())
