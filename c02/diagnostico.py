# Diagnóstico del entorno: versiones y programas externos
import platform
import shutil
import sys
from importlib.metadata import version

print("Sistema:", platform.system(), platform.machine())
print("Python :", sys.version.split()[0])

for paquete in ["manim", "numpy", "av", "manimpango", "pycairo"]:
    print(f"{paquete:>10}: {version(paquete)}")

for programa in ["latex", "dvisvgm"]:
    ruta = shutil.which(programa)
    estado = "encontrado" if ruta else "NO encontrado"
    print(f"{programa:>10}: {estado}")
