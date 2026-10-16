# Cuando una fórmula no compila, Manim deja el .tex y el .log en
# media/Tex/. Este programa provoca el error y lee el registro.
import re
from pathlib import Path
from manim import *

config.no_latex_cleanup = True        # conserva .log, .aux y .dvi
config.verbosity = "CRITICAL"         # silencia el aviso de Manim

try:
    MathTex(r"\frac{1}{2}+\sqr{2}")  # \sqr no existe
except ValueError as error:
    registro = Path(re.search(r"(media/Tex/\S+\.log)",
                              str(error)).group(1))
    lineas = registro.read_text(errors="replace").splitlines()
    print("registro:", registro.name)
    for k, linea in enumerate(lineas):
        if linea.startswith("!"):     # así empieza cada error
            print(linea)
            # la línea «l.N» dice en qué línea del .tex fue
            for sig in lineas[k + 1:k + 8]:
                if sig.startswith("l."):
                    print(sig)
                    break
            break
    fuente = registro.with_suffix(".tex").read_text()
    print("documento compilado:", registro.with_suffix(".tex").name)
    print(fuente.splitlines()[-3])    # la línea con la fórmula
