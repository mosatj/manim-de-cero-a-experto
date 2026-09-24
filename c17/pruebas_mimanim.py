"""Pruebas automáticas de las animaciones de mimanim.

Se ejecutan con  python pruebas_mimanim.py  (o con pytest).
"""
import tempfile

import numpy as np

from mimanim import (Contador, DecimalNumber, Latido, Square,
                     config, linear)

config.verbosity = "WARNING"             # sin mensajes informativos
config.media_dir = tempfile.mkdtemp()    # no ensuciar el proyecto


def prueba_contador_extremos():
    numero = DecimalNumber(0)
    anim = Contador(numero, 10, 20, rate_func=linear)
    anim.begin()
    anim.interpolate(0.5)
    assert abs(numero.get_value() - 15) < 1e-9
    anim.finish()
    assert numero.get_value() == 20


def prueba_latido_sin_memoria():
    cuadrado = Square()
    anim = Latido(cuadrado)
    anim.begin()
    anim.interpolate(0.3)
    a = cuadrado.points.copy()
    anim.interpolate(0.9)       # saltamos a otro fotograma...
    anim.interpolate(0.3)       # ...y volvemos: debe dar lo mismo
    assert np.allclose(a, cuadrado.points)


def prueba_latido_vuelve_al_inicio():
    cuadrado = Square()
    original = cuadrado.points.copy()
    anim = Latido(cuadrado)
    anim.begin()
    anim.finish()
    assert np.allclose(original, cuadrado.points)


if __name__ == "__main__":
    pruebas = [f for n, f in list(globals().items())
               if n.startswith("prueba_")]
    for prueba in pruebas:
        prueba()
        print(f"ok  {prueba.__name__}")
    print(f"{len(pruebas)} pruebas superadas")
