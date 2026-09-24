from manim import *

cuadrado = Square()
print(type(cuadrado.points).__name__, cuadrado.points.shape)
print(cuadrado.points[:4])          # la primera curva de Bézier
cuadrado.shift(RIGHT)               # por dentro: points += vector
print("tras shift:", cuadrado.points[0])
print("círculo:", Circle().points.shape)
