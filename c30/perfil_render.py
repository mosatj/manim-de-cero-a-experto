# Perfila solo el render de una escena y agrupa el tiempo por partes
import cProfile
import pstats
import sys
import tempfile

from manim import tempconfig

sys.path.insert(0, "proyecto")          # para importar sus escenas
from e02_demostracion import Demostracion

# (grupo, fragmento que aparece en el archivo o en la función)
GRUPOS = [("esperar a LaTeX", "waitpid"),
          ("codificar (PyAV)", "av."),
          ("texto (Pango)", "text_mobject"),
          ("dibujar (Cairo)", "cairo"),
          ("dibujar (Cairo)", "manim/camera"),
          ("copias", "copy.py"), ("mobjects", "manim/mobject"),
          ("NumPy", "numpy")]

opciones = {"quality": "medium_quality", "disable_caching": True,
            "media_dir": tempfile.mkdtemp(), "verbosity": "ERROR",
            "progress_bar": "none"}
with tempconfig(opciones):
    perfil = cProfile.Profile()
    perfil.runcall(Demostracion().render)
datos = pstats.Stats(perfil)
tiempos = dict.fromkeys([g for g, _ in GRUPOS] + ["otros"], 0.0)
for (archivo, _, funcion), valores in datos.stats.items():
    lugar = archivo + funcion
    grupo = next((g for g, c in GRUPOS if c in lugar), "otros")
    tiempos[grupo] += valores[2]      # tiempo propio de la función
print(f"Render de Demostracion (720p30): {datos.total_tt:.2f} s")
for grupo, t in sorted(tiempos.items(), key=lambda g: -g[1]):
    print(f"  {grupo:18} {t:5.2f} s  {t / datos.total_tt:5.1%}")
