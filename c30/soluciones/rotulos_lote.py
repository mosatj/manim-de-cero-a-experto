import sys
from pathlib import Path

from manim import *

# El rótulo del capítulo está en la carpeta superior
sys.path.append(str(Path(__file__).parent.parent))
from rotulo_inferior import RotuloInferior


class RotuloAjustado(RotuloInferior):
    """Si el texto no cabe en la zona segura, lo reduce."""

    def crear(self):
        barra, banda, textos = super().crear()
        limite = 0.9 * config.right_side[0]  # borde de la zona
        if banda.get_right()[0] > limite:
            factor = ((limite - textos.get_left()[0] - 0.55)
                      / textos.width)
            if factor < 32 / 34:  # el cargo bajaría de 32 puntos
                logger.warning(f"{self.nombre}: acorta el cargo")
            textos.scale(factor, about_edge=LEFT)
            banda.stretch_to_fit_width(textos.width + 1.1,
                                       about_edge=LEFT)
        return barra, banda, textos


class Rotulo01Rojas(RotuloAjustado):
    nombre = "Ana Rojas"
    cargo = "Estudiante de Ingeniería"


class Rotulo02Paredes(RotuloAjustado):
    nombre = "Luis Alberto Paredes Villanueva"
    cargo = ("Coordinador del Departamento de Ciencias "
             "Básicas y Matemática Aplicada")


class Rotulo03Vega(RotuloAjustado):
    nombre = "Carmen Vega"
    cargo = "Profesora invitada"
