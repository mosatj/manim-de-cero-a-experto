# Renderiza en paralelo todas las escenas del proyecto (-ql, último
# fotograma) y muestra cuánto tardó cada una
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

RAIZ = Path(__file__).parent.parent / "proyecto"
ESCENAS = sorted(RAIZ.glob("e[0-9][0-9]_*.py"))


def renderizar(archivo, carpeta):
    # Una carpeta media por proceso: si la comparten, dos procesos
    # pueden pisarse los archivos temporales de texto y de LaTeX
    propia = str(Path(carpeta) / archivo.stem)
    inicio = time.perf_counter()
    orden = [sys.executable, "-m", "manim", "-ql", "-s", "-a",
             "--media_dir", propia, archivo.name]
    r = subprocess.run(orden, cwd=RAIZ, capture_output=True,
                       text=True)
    estado = "bien" if r.returncode == 0 else "ERROR"
    return archivo.name, estado, time.perf_counter() - inicio


with tempfile.TemporaryDirectory() as carpeta:
    inicio = time.perf_counter()
    with ThreadPoolExecutor(max_workers=3) as grupo:
        tareas = [grupo.submit(renderizar, a, carpeta)
                  for a in ESCENAS]
        for tarea in tareas:
            nombre, estado, s = tarea.result()
            print(f"{nombre:22} {estado:6} {s:4.1f} s")
    imagenes = len(list(Path(carpeta).rglob("*.png")))
    total = time.perf_counter() - inicio
    print(f"{imagenes} imágenes en {total:.1f} s en total")
