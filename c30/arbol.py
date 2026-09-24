# Dibuja el árbol de carpetas del proyecto (sin cachés ni media/)
from pathlib import Path

IGNORAR = {"__pycache__", "media", ".venv"}


def arbol(carpeta, prefijo=""):
    hijos = sorted(p for p in carpeta.iterdir()
                   if p.name not in IGNORAR)
    for i, hijo in enumerate(hijos):
        ultimo = i == len(hijos) - 1
        rama = "└── " if ultimo else "├── "
        print(prefijo + rama + hijo.name)
        if hijo.is_dir():
            arbol(hijo, prefijo + ("    " if ultimo else "│   "))


print("proyecto/")
arbol(Path("proyecto"))
