"""Conversiones de ángulos (propuesto del capítulo 4)."""
import math


def a_radianes(grados):
    """Convierte grados sexagesimales a radianes."""
    return grados * math.pi / 180


def a_grados(radianes):
    """Convierte radianes a grados sexagesimales."""
    return radianes * 180 / math.pi


if __name__ == "__main__":
    print("Prueba:", a_radianes(180), a_grados(math.pi / 2))
