# Subtítulos en formato WebVTT (el de los reproductores web)
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from guion_impares import GUION, duracion  # noqa: E402
from subtitulos import repartir  # noqa: E402


def marca_vtt(segundos):
    """12.5 -> '00:00:12.500' (WebVTT usa punto, no coma)."""
    ms = round(segundos * 1000)
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"


lineas, t = ["WEBVTT", ""], 0.0
for bloque in GUION:
    d = duracion(bloque)
    for ini, fin, texto in repartir(bloque["voz"], t, d - 1.0):
        lineas += [f"{marca_vtt(ini)} --> {marca_vtt(fin)}", texto, ""]
    t += d
print("\n".join(lineas[:9]))
