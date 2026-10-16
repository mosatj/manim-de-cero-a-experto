"""importar_asy que sobrevive sin Asymptote: si no hay «asy» pero
sí un SVG ya generado, lo usa; si no hay nada, explica qué falta."""
import os
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from manim import *  # noqa: E402
import asy_puente  # noqa: E402


def importar_asy_robusto(ruta, **kwargs):
    asy = Path(ruta)
    svg = asy.with_suffix(".svg")
    if shutil.which("asy") is None:
        if svg.exists():
            print(f"aviso: sin Asymptote, se usa {svg.name}")
            return SVGMobject(svg, **kwargs)
        raise FileNotFoundError(
            f"No hay Asymptote instalado ni existe {svg}: instala "
            "asy o pide el SVG a quien hizo el dibujo.")
    return asy_puente.importar_asy(asy, **kwargs)


# Prueba: se esconde «asy» vaciando el PATH
figura = importar_asy_robusto("../asy_construccion.asy")
print("con asy:", len(figura), "partes")
camino = os.environ["PATH"]
os.environ["PATH"] = ""
figura = importar_asy_robusto("../asy_construccion.asy")
print("sin asy:", len(figura), "partes")
try:
    importar_asy_robusto("../no_existe.asy")
except FileNotFoundError as e:
    print("error claro:", str(e)[:48], "…")
os.environ["PATH"] = camino
