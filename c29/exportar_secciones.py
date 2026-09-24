# Renderiza con --save_sections y lee el índice JSON de Manim
import json
import subprocess
import sys
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as carpeta:
    subprocess.run([sys.executable, "-m", "manim", "-ql",
                    "--save_sections", "--media_dir", carpeta,
                    "presentacion_secciones.py",
                    "PresentacionSecciones"],
                   check=True, capture_output=True)
    indice = next(Path(carpeta).rglob("sections/*.json"))
    print("Índice:", indice.name)
    for s in json.loads(indice.read_text()):
        print(f"{s['name']:14}{s['video']:45}"
              f"{float(s['duration']):5.2f} s")
    videos = sorted(p.name for p in indice.parent.glob("*.mp4"))
    print("Vídeos:", len(videos))
