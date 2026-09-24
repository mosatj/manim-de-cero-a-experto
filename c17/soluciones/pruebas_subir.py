"""Pruebas de SubirYAparecer (se ejecutan sin renderizar nada)."""
import sys
import tempfile
from pathlib import Path

import numpy as np

# mimanim está en la carpeta padre de soluciones/
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mimanim import Scene, SubirYAparecer, Text, config  # noqa

config.verbosity = "WARNING"
config.media_dir = tempfile.mkdtemp()


def prueba_sin_memoria():
    texto = Text("abc")
    anim = SubirYAparecer(texto)
    anim.begin()
    anim.interpolate(0.4)
    piezas = texto.family_members_with_points()
    antes = [s.points.copy() for s in piezas]
    anim.interpolate(0.9)
    anim.interpolate(0.4)
    despues = [s.points for s in piezas]
    assert all(np.allclose(a, d) for a, d in zip(antes, despues))


def prueba_introductora():
    escena = Scene()
    texto = Text("abc")
    anim = SubirYAparecer(texto)
    anim._setup_scene(escena)             # lo que hace Scene.play
    assert texto in escena.mobjects


def prueba_estado_final():
    texto = Text("abc")
    piezas = texto.family_members_with_points()
    original = [s.points.copy() for s in piezas]
    anim = SubirYAparecer(texto)
    anim.begin()
    anim.finish()
    finales = [s.points for s in piezas]
    assert all(np.allclose(a, b) for a, b in zip(original, finales))


if __name__ == "__main__":
    for prueba in (prueba_sin_memoria, prueba_introductora,
                   prueba_estado_final):
        prueba()
        print("ok ", prueba.__name__)
