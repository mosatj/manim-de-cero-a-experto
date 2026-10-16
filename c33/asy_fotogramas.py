"""Fotogramas clave de Asymptote para un parámetro que cambia.

El .asy declara «real t=0; usersetting();» y la orden
«asy -u t=0.25» cambia t sin tocar el archivo. Cada fotograma se
guarda en una caché con el nombre del hash de (texto, t): solo se
compila lo que falta, y editar el .asy invalida lo anterior.
"""
import hashlib
import subprocess
from pathlib import Path

from manim import *


def fotograma(asy, t, cache="cache_asy") -> Path:
    """Ruta del SVG para ese t (lo compila si no existe)."""
    asy = Path(asy)
    huella = asy.read_bytes() + f"{t:.6f}".encode()
    clave = hashlib.sha1(huella).hexdigest()[:12]
    carpeta = asy.parent / cache
    carpeta.mkdir(exist_ok=True)
    svg = carpeta / f"{asy.stem}-{clave}.svg"
    if not svg.exists():
        orden = ["asy", "-f", "svg", "-u", f"t={t:.6f}",
                 "-o", str(svg.with_suffix("")), asy.name]
        subprocess.run(orden, cwd=asy.parent, check=True,
                       capture_output=True)
    return svg


def fotogramas_asy(asy, valores, grosor=4.0, **kwargs):
    """Un SVGMobject por valor; todos con la misma estructura."""
    lista = []
    for t in valores:
        mob = SVGMobject(fotograma(asy, t), **kwargs)
        for parte in mob:
            ancho = parte.get_stroke_width()
            parte.set_stroke(width=grosor * ancho)
        lista.append(mob)
    return lista
