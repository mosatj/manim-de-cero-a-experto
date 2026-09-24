"""Pruebas automáticas del proyecto.

Con pytest:      uv run pytest
Sin pytest:      python pruebas/test_componentes.py
"""
import sys
import tempfile
from pathlib import Path

# La raíz del proyecto: así se importa «componentes» sin pytest
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from manim import config, tempconfig  # noqa: E402

from componentes import CuadradoImpares, Tarjeta  # noqa: E402

# Los archivos temporales (LaTeX, imágenes) no ensucian el proyecto
config.media_dir = tempfile.mkdtemp()
config.verbosity = "ERROR"
config.progress_bar = "none"


def test_cada_capa_tiene_un_impar():
    capas = CuadradoImpares(6)
    assert [len(capa) for capa in capas] == [1, 3, 5, 7, 9, 11]


def test_el_total_es_un_cuadrado():
    for n in range(1, 10):
        assert sum(len(capa) for capa in CuadradoImpares(n)) == n**2


def test_la_tarjeta_envuelve_su_formula():
    tarjeta = Tarjeta("Área", r"A=\frac{b\cdot h}{2}")
    assert tarjeta.marco.width > tarjeta.formula.width
    assert tarjeta.marco.height > tarjeta.formula.height


def test_la_escena_renderiza():
    from e02_demostracion import Demostracion
    opciones = {"quality": "low_quality", "save_last_frame": True,
                "disable_caching": True}
    with tempconfig(opciones):
        escena = Demostracion()
        escena.render()
        imagen = escena.renderer.get_frame()
        fondo = config.background_color.to_int_rgb()
    assert imagen.shape == (480, 854, 4)
    assert list(imagen[5, 5, :3]) == list(fondo)  # esquina: fondo


if __name__ == "__main__":
    pruebas = [f for nombre, f in globals().items()
               if nombre.startswith("test_")]
    for prueba in pruebas:
        prueba()
        print("superada:", prueba.__name__)
    print(len(pruebas), "pruebas superadas")
