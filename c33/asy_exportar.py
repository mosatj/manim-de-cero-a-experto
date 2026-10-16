"""El camino inverso: un VMobject de Manim como dibujo de Asymptote.

Cada curva de Bézier cúbica de Manim se escribe con la sintaxis
«..controls P1 and P2..» de Asymptote: el PDF resultante es
vectorial y se incluye en un artículo con \\includegraphics.
"""
import subprocess
from pathlib import Path

from manim import *


def _pt(p, escala):
    return f"({p[0] * escala:.4f},{p[1] * escala:.4f})"


def caminos(mob: VMobject, escala: float) -> list[str]:
    """Un camino de Asymptote por cada subtrazado del mobject."""
    salida = []
    for puntos in mob.get_subpaths():
        tuplas = mob.get_cubic_bezier_tuples_from_points(puntos)
        partes = [_pt(tuplas[0][0], escala)]
        for _, c1, c2, fin in tuplas:
            partes.append(f"..controls {_pt(c1, escala)} and "
                          f"{_pt(c2, escala)}..{_pt(fin, escala)}")
        salida.append("".join(partes))
    return salida


def exportar(mob: VMobject, ruta, escala=1.0) -> int:
    """Escribe el .asy; devuelve cuántas órdenes de dibujo tiene."""
    lineas = ["// Generado desde Manim", "unitsize(1cm);"]
    for m in mob.family_members_with_points():
        relleno = m.get_fill_color().to_hex()[1:]
        trazo = m.get_stroke_color().to_hex()[1:]
        grosor = 0.4 * m.get_stroke_width()   # unidades Manim → bp
        for camino in caminos(m, escala):
            if m.get_fill_opacity() > 0:
                alfa = m.get_fill_opacity()
                orden = f'fill({camino}--cycle, rgb("{relleno}")'
                lineas.append(orden + f"+opacity({alfa:.2f}));")
            if m.get_stroke_width() > 0:
                lineas.append(f'draw({camino}, rgb("{trazo}")'
                              f"+{grosor:.2f}bp);")
    Path(ruta).write_text("\n".join(lineas) + "\n")
    return len(lineas) - 2


if __name__ == "__main__":
    # Colores pensados para papel blanco, no para la pantalla
    tinta = "#1D1F22"
    ejes = Axes(x_range=[-3, 3], y_range=[-1.5, 1.5], x_length=6,
                y_length=3, axis_config={"color": tinta})
    f = lambda x: np.sin(2 * x) * np.exp(-0.2 * x * x)
    curva = ejes.plot(f, color="#4F7C99")
    area = ejes.get_area(curva, x_range=[-1.5, 1.5],
                         color="#4F7C99", opacity=0.3)
    n = exportar(VGroup(ejes, area, curva), "asy_exportado.asy")
    subprocess.run(["asy", "-f", "pdf", "asy_exportado.asy"],
                   check=True)
    subprocess.run(["gs", "-q", "-sDEVICE=png16m", "-r200", "-o",
                    "asy_exportado.png", "asy_exportado.pdf"],
                   check=True)
    print(f"asy_exportado.asy: {n} órdenes de dibujo")
    print("asy_exportado.pdf y asy_exportado.png generados")
