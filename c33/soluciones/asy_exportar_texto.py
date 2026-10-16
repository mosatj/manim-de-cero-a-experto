"""Texto y fórmulas de Manim exportados a Asymptote: también son
curvas de Bézier, así que el mismo exportador sirve."""
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from manim import *  # noqa: E402
from asy_exportar import exportar  # noqa: E402

config.verbosity = "ERROR"          # sin mensajes de LaTeX
config.media_dir = tempfile.mkdtemp()

formula = MathTex(r"e^{i\pi}+1=0", color="#1D1F22").scale(1.5)
estrella = Star(n=5, outer_radius=0.8, color="#B04A5A",
                fill_opacity=0.25).next_to(formula, RIGHT, buff=0.6)
n = exportar(VGroup(formula, estrella), "asy_texto.asy")
subprocess.run(["asy", "-f", "pdf", "asy_texto.asy"], check=True)
glifos = len(formula.family_members_with_points())
print(f"{glifos} glifos + 1 estrella → {n} órdenes de dibujo")
print("asy_texto.pdf generado")
