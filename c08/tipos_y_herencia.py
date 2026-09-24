from manim import *

punto = Dot()
print("type(punto):", type(punto).__name__)
print("¿Es un Circle?  ", isinstance(punto, Circle))
print("¿Es un VMobject?", isinstance(punto, VMobject))
print("¿Es una Scene?  ", isinstance(punto, Scene))
print()
print("Orden de resolución de métodos (MRO) de Dot:")
for clase in Dot.mro():
    print("   ", clase.__module__, "->", clase.__name__)
