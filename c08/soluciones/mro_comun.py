from manim import *


def ancestro_comun(a, b):
    """Primera clase del MRO de a que también está en b."""
    for clase in a.mro():
        if clase in b.mro():
            return clase.__name__


for clase in [Star, RoundedRectangle, SurroundingRectangle]:
    print(clase.__name__, ":",
          " > ".join(c.__name__ for c in clase.mro()[:-1]))
    comun = ancestro_comun(clase, Square)
    print("   común con Square:", comun)
