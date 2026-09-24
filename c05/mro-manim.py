from manim import *

# Las cadenas de herencia reales de algunas clases de Manim
for clase in [Square, Dot, VGroup, Create]:
    # mro()[:-1] omite object, la raíz común de todo
    cadena = " → ".join(k.__name__ for k in clase.mro()[:-1])
    print(f"{clase.__name__:>6}: {cadena}")
print("¿Un Dot es un Circle?", issubclass(Dot, Circle))
print("¿Un Square es un Mobject?", isinstance(Square(), Mobject))
