from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class FamiliasColor(Scene):
    def construct(self):
        familias = ["BLUE", "TEAL", "GREEN", "YELLOW", "GOLD",
                    "RED", "MAROON", "PURPLE", "GRAY"]
        filas = VGroup()
        for fam in familias:
            fila = VGroup(Text(fam, font_size=26))
            for tono in "ABCDE":
                color = globals()[f"{fam}_{tono}"]  # p. ej. BLUE_C
                fila.add(Rectangle(width=1.5, height=0.6,
                                   stroke_width=0, fill_opacity=1,
                                   fill_color=color))
            fila[1:].arrange(RIGHT, buff=0.1)
            fila[0].next_to(fila[1], LEFT, buff=0.3)
            filas.add(fila)
        filas.arrange(DOWN, buff=0.12, aligned_edge=RIGHT)
        cabecera = VGroup(*[Text(f"_{t}", font_size=26)
                            .next_to(filas[0][k + 1], UP)
                            for k, t in enumerate("ABCDE")])
        self.add(filas, cabecera)
