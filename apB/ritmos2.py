from manim import *
from ritmos1 import celda

FAMILIAS = ["sine", "quad", "cubic", "quart", "quint"]


class RitmosEstandarA(Scene):
    def construct(self):
        # Filas: ease_in, ease_out, ease_in_out; columnas: familias
        celdas = VGroup()
        for tipo in ["in", "out", "in_out"]:
            for familia in FAMILIAS:
                nombre = f"ease_{tipo}_{familia}"
                celdas.add(celda(getattr(rate_functions, nombre), nombre))
        celdas.arrange_in_grid(rows=3, cols=5, buff=(0.3, 0.3))
        # que quepa a lo ancho y a lo alto del fotograma
        celdas.scale(min(13.4 / celdas.width, 7.5 / celdas.height))
        self.add(celdas.move_to(ORIGIN))
