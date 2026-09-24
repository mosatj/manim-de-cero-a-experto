from manim import *


class Paleta:
    """Colores con significado: se nombran por su papel."""
    DATO = ManimColor("#56B4E9")        # azul cielo (Okabe e Ito)
    INCOGNITA = ManimColor("#E69F00")   # naranja
    RESULTADO = ManimColor("#F0E442")   # amarillo
    AUXILIAR = ManimColor("#999999")    # gris: lo que acompaña

    @classmethod
    def roles(cls):
        return {"dato": cls.DATO, "incógnita": cls.INCOGNITA,
                "resultado": cls.RESULTADO, "auxiliar": cls.AUXILIAR}


def gris_equivalente(color):
    """El gris con la misma luminancia: así lo vería una fotocopia."""
    r, g, b = color.to_rgb()
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return ManimColor.from_rgb((y, y, y))


class PaletaSemantica(Scene):
    def construct(self):
        filas = VGroup()
        for rol, color in Paleta.roles().items():
            muestra = Square(1.1, fill_color=color, fill_opacity=1,
                             stroke_width=0)
            gris = muestra.copy().set_fill(gris_equivalente(color))
            nombre = Text(rol, font_size=34, color=color)
            fila = VGroup(nombre, muestra, gris)
            filas.add(fila.arrange(RIGHT, buff=0.6))
        filas.arrange(DOWN, buff=0.35, aligned_edge=RIGHT)
        cabecera = VGroup(Text("color", font_size=26, color=GREY_B),
                          Text("en gris", font_size=26, color=GREY_B))
        for texto, columna in zip(cabecera, (1, 2)):
            texto.next_to(filas[0][columna], UP)
        self.play(LaggedStart(*[FadeIn(f, shift=RIGHT) for f in filas]),
                  FadeIn(cabecera))
