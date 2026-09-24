# Compara el tiempo de render de always_redraw frente a un updater
import subprocess
import sys
import tempfile
import time

for archivo, escena in [("redibujo_lento.py", "RedibujoLento"),
                        ("redibujo_rapido.py", "RedibujoRapido")]:
    with tempfile.TemporaryDirectory() as carpeta:
        inicio = time.perf_counter()
        subprocess.run([sys.executable, "-m", "manim", "-qh",
                        "--disable_caching", "--media_dir", carpeta,
                        archivo, escena],
                       check=True, capture_output=True)
        print(f"{escena:15} {time.perf_counter() - inicio:5.2f} s")
