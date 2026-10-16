"""Puente Asymptote → Manim.

importar_asy(ruta)      compila un .asy a SVG → SVGMobject
importar_asy_png(ruta)  con sombreados: PDF → PNG → ImageMobject
Las dos recompilan solo si el .asy es más nuevo que su salida.
"""
import subprocess
from pathlib import Path

from manim import *


def _desactualizado(salida: Path, fuente: Path) -> bool:
    # Falta la salida, o el .asy se editó después de generarla
    return (not salida.exists()
            or salida.stat().st_mtime < fuente.stat().st_mtime)


def _compilar(asy: Path, formato: str) -> None:
    # Asymptote escribe la salida junto al .asy, con su mismo nombre
    orden = ["asy", "-f", formato, asy.name]
    subprocess.run(orden, cwd=asy.parent, check=True)


def importar_asy(ruta, grosor=4.0, **kwargs) -> SVGMobject:
    """SVGMobject a partir de un .asy (dibujos planos, alambres 3D).

    Asymptote mide los grosores en puntos de impresora; en Manim el
    trazo normal mide 4: por eso se multiplican por «grosor»."""
    asy = Path(ruta)
    svg = asy.with_suffix(".svg")
    if _desactualizado(svg, asy):
        _compilar(asy, "svg")
    figura = SVGMobject(svg, **kwargs)
    for parte in figura:
        parte.set_stroke(width=parte.get_stroke_width() * grosor)
    return figura


def importar_asy_png(ruta, dpi=300, height=None) -> ImageMobject:
    """ImageMobject de un .asy con sombreados: PDF y Ghostscript."""
    asy = Path(ruta)
    pdf, png = asy.with_suffix(".pdf"), asy.with_suffix(".png")
    if _desactualizado(png, asy):
        _compilar(asy, "pdf")
        subprocess.run(["gs", "-q", "-sDEVICE=pngalpha", f"-r{dpi}",
                        "-o", str(png), str(pdf)], check=True)
    imagen = ImageMobject(png)
    if height is not None:
        imagen.height = height
    return imagen
