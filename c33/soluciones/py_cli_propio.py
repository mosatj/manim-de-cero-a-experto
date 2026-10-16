# Un «manim» propio: elige secciones y calidad desde la terminal
#   python py_cli_propio.py --secciones A C --calidad l
import argparse
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from manim import tempconfig          # noqa: E402
import py_tarjeta                     # noqa: E402

CALIDADES = {"l": "low_quality", "m": "medium_quality",
             "h": "high_quality"}
parser = argparse.ArgumentParser()
parser.add_argument("--secciones", nargs="+", default=["A"])
parser.add_argument("--calidad", choices=CALIDADES, default="l")
args = parser.parse_args()

carpeta = tempfile.mkdtemp()
for seccion in args.secciones:
    Escena = type(f"Tarjeta{seccion}", (py_tarjeta.TarjetaSeccion,),
                  {"seccion": seccion})
    with tempconfig({"quality": CALIDADES[args.calidad],
                     "media_dir": carpeta, "verbosity": "ERROR",
                     "progress_bar": "none",
                     "output_file": f"tarjeta_{seccion}"}):
        Escena().render()
for v in sorted(Path(carpeta).rglob("*.mp4")):
    if "partial" not in str(v):
        print("listo:", v.name)
