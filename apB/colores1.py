from manim import *

FAMILIAS = ["BLUE", "TEAL", "GREEN", "YELLOW", "GOLD",
            "RED", "MAROON", "PURPLE", "GRAY"]


def muestra(nombre, ancho=1.45, alto=1.2):
    """Rectángulo del color «nombre» con su nombre y su código hex."""
    color = globals()[nombre]              # la constante de Manim
    caja = Rectangle(width=ancho, height=alto, fill_color=color,
                     fill_opacity=1, stroke_color=GRAY_B, stroke_width=1)
    tinta = color.contrasting()            # negro o blanco, lo que se lea
    rotulo = VGroup(Text(nombre, font="Menlo", font_size=15, color=tinta),
                    Text(color.to_hex(), font="Menlo", font_size=13,
                         color=tinta)).arrange(DOWN, buff=0.08)
    if rotulo.width > 0.92 * ancho:
        rotulo.scale_to_fit_width(0.92 * ancho)
    return VGroup(caja, rotulo.move_to(caja))


class ColoresFamilias(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # Columnas: familias; filas: tonos de A (claro) a E (oscuro)
        columnas = VGroup(*[
            VGroup(*[muestra(f"{fam}_{t}") for t in "ABCDE"])
            .arrange(DOWN, buff=0.08)
            for fam in FAMILIAS]).arrange(RIGHT, buff=0.08)
        self.add(columnas.scale_to_fit_width(13.8).move_to(ORIGIN))
