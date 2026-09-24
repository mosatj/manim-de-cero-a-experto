from manim import *
from colores1 import muestra

OTROS = ["WHITE", "LIGHTER_GRAY", "LIGHT_GRAY", "DARK_GRAY", "DARKER_GRAY",
         "BLACK", "PURE_RED", "PURE_GREEN", "PURE_BLUE", "PURE_CYAN",
         "PURE_MAGENTA", "PURE_YELLOW", "ORANGE", "PINK", "LIGHT_PINK",
         "LIGHT_BROWN", "DARK_BROWN", "GRAY_BROWN", "DARK_BLUE", "LOGO_WHITE",
         "LOGO_GREEN", "LOGO_BLUE", "LOGO_RED", "LOGO_BLACK"]


class ColoresOtros(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        muestras = VGroup(*[muestra(n, ancho=2.2, alto=1.5) for n in OTROS])
        muestras.arrange_in_grid(rows=4, cols=6, buff=0.12)
        self.add(muestras.scale_to_fit_width(13.8).move_to(ORIGIN))
