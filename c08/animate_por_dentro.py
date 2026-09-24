from manim import *

cuadrado = Square()
constructor = cuadrado.animate
print("1)", type(constructor).__name__)
print("   ¿Hay objetivo?", cuadrado.target is not None)

constructor.shift(RIGHT * 2).scale(0.5)
print("2) Métodos anotados:",
      [m.method.__name__ for m in constructor.methods])
print("   Centro del original:", cuadrado.get_center())
print("   Centro del objetivo:", cuadrado.target.get_center())

animacion = constructor.build()
print("3)", " > ".join(c.__name__
                       for c in type(animacion).mro()[:-1]))
try:
    cuadrado.animate.shift(UP)(run_time=2)
except ValueError as error:
    print("4) ValueError:", error)
