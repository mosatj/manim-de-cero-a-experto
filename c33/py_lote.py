# Un vídeo por sección, sin tocar la escena: fábrica de escenas
import tempfile
import time
from pathlib import Path

from manim import tempconfig
from py_tarjeta import TarjetaSeccion, DATOS

COLORES = {"A": "#6FA3C0", "B": "#E0B04A", "C": "#B04A5A"}
carpeta = tempfile.mkdtemp()
ajustes = {"quality": "low_quality", "media_dir": carpeta,
           "verbosity": "ERROR", "progress_bar": "none",
           "disable_caching": True}
inicio = time.perf_counter()
for seccion in sorted(DATOS["seccion"].unique()):
    # Una subclase nueva por sección, creada con type()
    Escena = type(f"Tarjeta{seccion}", (TarjetaSeccion,),
                  {"seccion": seccion, "color": COLORES[seccion]})
    salida = {**ajustes, "output_file": f"seccion_{seccion}"}
    with tempconfig(salida):
        Escena().render()
# Solo los vídeos finales (no los parciales de la caché)
videos = sorted(v for v in Path(carpeta).rglob("*.mp4")
                if "partial" not in str(v))
for v in videos:
    print(f"{v.name:16}{v.stat().st_size / 1024:6.0f} KB")
segundos = time.perf_counter() - inicio
print(f"{len(videos)} vídeos en {segundos:.1f} s")
