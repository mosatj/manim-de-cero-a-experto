"""Pruebas mínimas del proyecto.

Con pytest:      uv run pytest
Sin pytest:      python pruebas/test_proyecto.py
"""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from manim import config, tempconfig  # noqa: E402

import guion  # noqa: E402
from componentes import Tarjeta  # noqa: E402

config.media_dir = tempfile.mkdtemp()
config.verbosity = "ERROR"
config.progress_bar = "none"


def test_el_guion_dura_lo_previsto():
    total = sum(guion.duracion(clave) for clave, _ in guion.FRASES)
    assert 5 < total < 20


def test_la_tarjeta_envuelve_su_rotulo():
    tarjeta = Tarjeta("Prueba")
    assert tarjeta.marco.width > tarjeta.rotulo.width


def test_la_escena_renderiza():
    from e01_gancho import Gancho
    opciones = {"quality": "low_quality", "format": "png",
                "disable_caching": True}
    with tempconfig(opciones):
        escena = Gancho()  # la escena se crea DENTRO del bloque
        escena.render()
        alto, ancho, _ = escena.renderer.get_frame().shape
    assert (ancho, alto) == (854, 480)


if __name__ == "__main__":
    pruebas = [f for nombre, f in list(globals().items())
               if nombre.startswith("test_")]
    for prueba in pruebas:
        prueba()
        print("superada:", prueba.__name__)
    print(len(pruebas), "pruebas superadas")
