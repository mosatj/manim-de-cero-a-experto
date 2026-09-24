from manim import *

for figura in [Triangle(), Line(), Dot(), Square(),
               RegularPolygon(n=6)]:
    n = len(figura.points)
    print(f"{type(figura).__name__:>14}: {n:2d} puntos,",
          f"{figura.get_num_curves()} curvas")
