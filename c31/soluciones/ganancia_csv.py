# Ejercicio 31.9: el mismo análisis de ganancia_normalizada.py, pero con
# las notas leídas de un CSV (columnas grupo,pre,post) en lugar de simularlas.
# El archivo notas.csv que acompaña a este programa es solo un ejemplo.
import csv
from pathlib import Path

import numpy as np

ARCHIVO = Path(__file__).with_name("notas.csv")


def leer_notas(ruta):
    """Devuelve {grupo: (pre, post)} con arreglos de NumPy."""
    datos = {}
    with open(ruta, newline="", encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            pre, post = datos.setdefault(fila["grupo"], ([], []))
            pre.append(fila["pre"])
            post.append(fila["post"])
    return {
        g: (np.array(pre, dtype=float), np.array(post, dtype=float))
        for g, (pre, post) in datos.items()
    }


# Las dos funciones no cambian: están separadas de los datos
def ganancia(pre, post):
    """Ganancia normalizada de Hake (medias del grupo, 0-100)."""
    return (post.mean() - pre.mean()) / (100 - pre.mean())


def d_cohen(x, y):
    """Diferencia de medias / desviación típica combinada."""
    nx, ny = len(x), len(y)
    s = np.sqrt(
        ((nx - 1) * x.var(ddof=1) + (ny - 1) * y.var(ddof=1))
        / (nx + ny - 2)
    )
    return (x.mean() - y.mean()) / s


notas = leer_notas(ARCHIVO)
print(f"Datos de {ARCHIVO.name}")
for nombre, (pre, post) in sorted(notas.items()):
    # Con pocos estudiantes, el d de Cohen es poco fiable: se informa n
    print(
        f"Grupo {nombre} (n = {len(pre)}): pre = {pre.mean():5.1f}  "
        f"post = {post.mean():5.1f}  <g> = {ganancia(pre, post):.2f}"
    )
(pre_a, post_a), (pre_b, post_b) = notas["A"], notas["B"]
print(f"d de Cohen (mejoras): {d_cohen(post_a - pre_a, post_b - pre_b):.2f}")
