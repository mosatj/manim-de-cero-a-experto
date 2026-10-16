from manim import *
from manim.utils.tex_file_writing import tex_to_svg_file


def plantilla_tikz(*bibliotecas, paquetes=""):
    """Plantilla de LaTeX preparada para TikZ. La primera línea es
    imprescindible: sin el driver de dvisvgm, pgf emite los dibujos
    como órdenes PostScript que dvisvgm no entiende y solo
    sobreviven los textos."""
    plantilla = TexTemplate()
    plantilla.add_to_preamble(
        r"\def\pgfsysdriver{pgfsys-dvisvgm.def}"
        + r"\usepackage{tikz}" + paquetes
        + r"\usetikzlibrary{" + ",".join(bibliotecas) + "}",
        prepend=True,
    )
    return plantilla


def figura_tikz(codigo, entorno="tikzpicture", plantilla=None,
                tinta=WHITE, fondo=BLACK, grosor=5, **kwargs):
    """Compila código de TikZ y lo devuelve como SVGMobject.

    Se usa el SVG completo (no Tex, que ignora los trazos y solo
    conserva el primer grupo). Lo que TikZ dibuja en negro pasa al
    color «tinta» para verse sobre el fondo de Manim, y lo blanco
    (cajas de leyendas) al color «fondo»; los demás se respetan.
    Los grosores de TikZ se multiplican por
    «grosor»: la línea fina de 0,4 pt pasa a 2 de Manim."""
    plantilla = plantilla or plantilla_tikz()
    archivo = tex_to_svg_file(codigo, entorno, plantilla)
    figura = SVGMobject(archivo, **kwargs)
    for parte in figura.family_members_with_points():
        rellena = parte.get_fill_opacity() > 0
        if rellena and parte.get_fill_color() == BLACK:
            parte.set_fill(tinta)
        elif rellena and parte.get_fill_color() == WHITE:
            parte.set_fill(fondo)
        if parte.get_stroke_width() > 0:
            if parte.get_stroke_color() == BLACK:
                parte.set_stroke(tinta)
            ancho = parte.get_stroke_width() * grosor
            parte.set_stroke(width=ancho)
    return figura
