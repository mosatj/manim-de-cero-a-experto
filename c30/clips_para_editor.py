# Renderiza un clip por sección y lo nombra para el editor
import json
import shutil
import subprocess
import sys
import tempfile
from fractions import Fraction
from pathlib import Path

LECCION, ESCENA = "L03", "E02"  # códigos de la escaleta


def timecode(fotogramas, fps):
    """Código de tiempo hh:mm:ss:ff, como lo muestra el editor."""
    s, ff = divmod(fotogramas, fps)
    return f"{s // 3600:02}:{s // 60 % 60:02}:{s % 60:02}:{ff:02}"


with tempfile.TemporaryDirectory() as tmp:
    subprocess.run([sys.executable, "-m", "manim", "-ql",
                    "--fps", "30", "--save_sections",
                    "--media_dir", tmp, "secciones_montaje.py",
                    "PendienteTangente"],
                   check=True, capture_output=True)
    indice = next(Path(tmp).rglob("sections/*.json"))
    destino = Path(tmp) / "montaje" / "02_manim"
    destino.mkdir(parents=True)
    entrada = 0  # fotograma en que empieza cada clip
    for i, s in enumerate(json.loads(indice.read_text()), 1):
        nombre = f"{LECCION}_{ESCENA}_S{i:02}_{s['name']}.mp4"
        shutil.copy(indice.parent / s["video"], destino / nombre)
        fps = Fraction(s["avg_frame_rate"])
        n = int(s["nb_frames"])
        print(f"{nombre:30}{n:4} fot.  entra en "
              f"{timecode(entrada, int(fps))}")
        entrada += n
    print(f"Total: {entrada} fotogramas a {fps} fps "
          f"= {entrada / fps:.2f} s")
