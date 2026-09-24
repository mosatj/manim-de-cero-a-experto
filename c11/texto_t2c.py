from manim import *


class TextoT2C(Scene):
    def construct(self):
        # t2c, «texto a color»: claves con palabras o rebanadas
        frase = Text(
            "La derivada mide el cambio",
            t2c={"derivada": YELLOW, "[18:27]": BLUE},
            font_size=44,
        )
        # t2w y t2s: peso e inclinación solo para algunas palabras
        enfasis = Text(
            "Un concepto clave, dicho con calma",
            t2w={"clave": BOLD}, t2s={"calma": ITALIC},
            font_size=40,
        )
        # Degradado de izquierda a derecha
        degradado = Text("Degradado", gradient=(BLUE, GREEN, RED),
                         font_size=72)
        # Indexar: los espacios NO cuentan como glifos
        indexado = Text("a b c", font_size=64)
        indexado[1].set_color(RED)  # la «b», no el espacio
        grupo = VGroup(frase, enfasis, degradado, indexado)
        self.add(grupo.arrange(DOWN, buff=0.55))
