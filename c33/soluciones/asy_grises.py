"""¿Qué color llega al SVG? Una recta con la pluma por defecto y
otra con pluma explícita, para cuatro plumas por defecto."""
import re
import subprocess
import tempfile
from pathlib import Path

plumas = ["white", "gray(0.6)", 'rgb("FFFFFF")', 'rgb("999999")']
print(f"{'defaultpen':>15}   sin pluma   con pluma")
for pluma in plumas:
    with tempfile.TemporaryDirectory() as carpeta:
        asy = Path(carpeta) / "plumas.asy"
        asy.write_text(f"size(3cm); defaultpen({pluma});\n"
                       "draw((0,0)--(4,0));\n"           # sin pluma
                       f"draw((0,1)--(4,1), {pluma});\n")
        subprocess.run(["asy", "-f", "svg", asy.name], cwd=carpeta,
                       check=True, capture_output=True)
        svg = asy.with_suffix(".svg").read_text()
    sin, con = re.findall(r"stroke='(#[0-9a-f]+)'", svg)
    print(f"{pluma:>15}   {sin:>9}   {con:>9}")
