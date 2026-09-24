"""mimanim: mini-biblioteca de componentes propios para Manim 0.21.

Reexporta Manim, así que en un proyecto basta con
    from mimanim import *
para tener Manim y los componentes propios a la vez.
"""
from manim import *  # noqa: F401,F403

from .animaciones import (Contador, DibujarConLapiz, Latido,
                          SubirYAparecer)
from .escenas import PlantillaScene
from .herramientas import tira_de_muestras
from .mobjects import Medidor, Resorte
from .ritmos import escalones, pasarse_y_volver

__version__ = "0.1.0"
