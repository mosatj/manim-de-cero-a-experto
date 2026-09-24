# Mide el efecto de la caché: el mismo render tres veces
import subprocess
import sys
import tempfile
import time

ESCENA = ["e02_demostracion.py", "Demostracion"]


def renderizar(carpeta, *extra):
    inicio = time.perf_counter()
    orden = [sys.executable, "-m", "manim", "-qh", *extra,
             "--media_dir", carpeta, *ESCENA]
    r = subprocess.run(orden, cwd="proyecto", capture_output=True,
                       text=True)
    segundos = time.perf_counter() - inicio
    reutilizadas = (r.stdout + r.stderr).count("Using cached")
    return segundos, reutilizadas


with tempfile.TemporaryDirectory() as carpeta:
    pruebas = [("primera vez", ()), ("segunda vez", ()),
               ("sin caché", ("--disable_caching",))]
    for nombre, extra in pruebas:
        s, n = renderizar(carpeta, *extra)
        print(f"{nombre:12} {s:5.1f} s  animaciones de caché: {n}")
