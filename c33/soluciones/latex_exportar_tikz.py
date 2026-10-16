# De Manim a TikZ: cada VMobject es una lista de curvas de Bézier
# cúbicas (capítulo 8); TikZ las dibuja con «.. controls .. ..».
from manim import *


def a_tikz(mobject, escala=1.0, decimales=3):
    """Devuelve un \\draw de TikZ por cada pieza con puntos."""
    lineas = []
    for parte in mobject.family_members_with_points():
        color = parte.get_stroke_color().to_hex()[1:]
        grosor = parte.get_stroke_width() / 4
        estilo = (f"\\definecolor{{c}}{{HTML}}{{{color}}}"
                  f"\\draw[c,line width={grosor}pt]")
        puntos = parte.points * escala
        inicio = puntos[0]
        d = decimales
        par = lambda p: f"({p[0]:.{d}f},{p[1]:.{d}f})"
        trozos = [par(inicio)]
        for _, b, c, fin in zip(*[puntos[k::4] for k in range(4)]):
            trozos.append(f" .. controls {par(b)} and {par(c)}"
                          f" .. {par(fin)}")
        lineas.append(estilo + "".join(trozos) + ";")
    return "\n".join(lineas)


figura = VGroup(Star(5, outer_radius=1.5, color=RED),
                Circle(radius=1.5, color=BLUE))
tikz = a_tikz(figura)
with open("figura_manim.tikz", "w") as archivo:
    archivo.write(tikz)
print(tikz.count("\\draw"), "trazos;", len(tikz), "caracteres")
print(tikz[:220] + "...")
