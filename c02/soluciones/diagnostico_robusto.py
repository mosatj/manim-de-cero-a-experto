# Diagnóstico que no se detiene si falta un paquete
import platform
import shutil
import sys
from importlib.metadata import PackageNotFoundError, version

print("Sistema:", platform.system(), platform.machine())
print("Python :", sys.version.split()[0])

paquetes = ["manim", "numpy", "av", "manimpango", "pycairo",
            "manim-slides"]
for paquete in paquetes:
    try:
        texto = version(paquete)
    except PackageNotFoundError:
        texto = "no instalado"
    print(f"{paquete:>12}: {texto}")

for programa in ["latex", "dvisvgm"]:
    ruta = shutil.which(programa)
    estado = "encontrado" if ruta else "NO encontrado"
    print(f"{programa:>12}: {estado}")
