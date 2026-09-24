# ¿Es reproducible el render? Compara la huella (hash) de la imagen
import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path


def huella(*extra):
    with tempfile.TemporaryDirectory() as carpeta:
        subprocess.run([sys.executable, "-m", "manim", "-ql", "-s",
                        *extra, "--media_dir", carpeta,
                        "puntos_azar.py", "PuntosAzar"],
                       check=True, capture_output=True)
        png = next(Path(carpeta).rglob("*.png"))
        return hashlib.sha256(png.read_bytes()).hexdigest()[:12]


PRUEBAS=[(), (), ("--seed", "7"), ("--seed", "7"), ("--seed", "8")]
for extra in PRUEBAS:
    print(f"{' '.join(extra) or 'sin semilla':12} {huella(*extra)}")
