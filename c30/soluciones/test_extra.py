"""Pruebas nuevas para proyecto/pruebas/test_componentes.py."""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "proyecto"))
from manim import config  # noqa: E402  (antes que los componentes)

from componentes import CuadradoImpares  # noqa: E402


def test_el_lado_mide_n_por_lado():
    for n in range(1, 7):
        cuadro = CuadradoImpares(n, lado=0.4)
        assert abs(cuadro.width - n * 0.4) < 1e-9
        assert abs(cuadro.height - n * 0.4) < 1e-9


def test_esta_centrado():
    assert abs(CuadradoImpares(4).get_center()).max() < 1e-9


if __name__ == "__main__":
    config.verbosity = "ERROR"
    test_el_lado_mide_n_por_lado()
    test_esta_centrado()
    print("2 pruebas superadas")
