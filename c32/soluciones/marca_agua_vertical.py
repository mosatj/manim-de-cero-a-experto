import sys
from pathlib import Path

# Los módulos del proyecto 4 están en otra carpeta: se añade
# esa carpeta a la ruta de búsqueda de módulos
RAIZ = Path(__file__).resolve().parent.parent  # codigo/c32
sys.path.insert(0, str(RAIZ / "proyecto4"))
import formato_vertical as fv  # fija el formato 9:16
from manim import *


class CapsulaConMarca(Scene):
    def construct(self):
        marca = Text(
            "@matematica.animada", font_size=34, color=GREY_B
        ).set_opacity(0.8)
        # Dentro de la zona segura, justo sobre el margen inferior
        marca.to_edge(DOWN, buff=fv.MARGEN_ABAJO)
        titulo = fv.arriba(
            fv.lineas(
                "Identidades", "en 30 segundos", tam=fv.TAM_GANCHO
            )
        )
        self.add(fv.zona_segura())
        self.play(Write(titulo), FadeIn(marca))
