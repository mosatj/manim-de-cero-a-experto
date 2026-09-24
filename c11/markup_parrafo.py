from manim import *


class MarkupParrafo(Scene):
    def construct(self):
        # MarkupText: etiquetas al estilo HTML (lenguaje de Pango)
        marcado = MarkupText(
            'Texto en <b>negrita</b>, en <i>cursiva</i>, '
            '<span fgcolor="#58C4DD">azul</span> y '
            '<span underline="double">subrayado</span>.',
            font_size=34,
        )
        # H<sub>2</sub>O y x<sup>2</sup>: subíndices sin LaTeX
        quimica = MarkupText("H<sub>2</sub>O y x<sup>2</sup>",
                             font_size=60)
        # Paragraph: una línea por argumento, con alineación
        parrafo = Paragraph(
            "Cada argumento",
            "es una línea;",
            "se alinean a la derecha.",
            alignment="right", font_size=36, line_spacing=0.8,
        )
        grupo = VGroup(marcado, quimica, parrafo)
        self.add(grupo.arrange(DOWN, buff=0.7))
