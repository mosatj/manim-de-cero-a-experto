#!/usr/bin/env python3
"""Renderiza (fotograma final, calidad baja) todas las escenas del repositorio.

    python renderizar_todo.py            # todo
    python renderizar_todo.py c13 c14    # solo esos capítulos

Los resultados quedan en la carpeta media/ de cada capítulo. Los programas que no
usan Manim se ejecutan con Python y se muestra lo que imprimen.
"""
import ast
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent


def escenas(fuente):
    clases = {n.name: [ast.unparse(b) for b in n.bases]
              for n in ast.parse(fuente).body if isinstance(n, ast.ClassDef)}

    def es_escena(nombre, vistos=()):
        for base in clases.get(nombre, []):
            if base.endswith(("Scene", "Slide")):
                return True
            if base in clases and base not in vistos and es_escena(base, vistos + (nombre,)):
                return True
        return False
    return [n for n in clases if es_escena(n) and not n.startswith("_") and not n.endswith("Base")]


def main():
    filtros = sys.argv[1:]
    fallos = 0
    for py in sorted(RAIZ.glob("*/**/*.py")):
        rel = py.relative_to(RAIZ)
        if filtros and rel.parts[0] not in filtros:
            continue
        if "__pycache__" in rel.parts or "media" in rel.parts:
            continue
        fuente = py.read_text(encoding="utf-8")
        if re.search(r"^\s*(from manim|import manim)", fuente, re.M):
            for escena in escenas(fuente):
                print(f"▶ {rel} :: {escena}")
                r = subprocess.run([sys.executable, "-m", "manim", "-ql", "-s", py.name, escena],
                                   cwd=py.parent)
                fallos += r.returncode != 0
        else:
            print(f"▶ {rel} (Python)")
            r = subprocess.run([sys.executable, py.name], cwd=py.parent)
            fallos += r.returncode != 0
    print("Listo." if not fallos else f"Terminado con {fallos} fallos.")


if __name__ == "__main__":
    main()
