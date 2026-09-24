from manim import *

cuadrado = Square(side_length=2)
print("Forma del array de puntos:", cuadrado.points.shape)
print("Puntos por curva:", cuadrado.n_points_per_cubic_curve)
# Cada bloque de 4 filas es una curva de Bézier cúbica
curvas = cuadrado.points.reshape(-1, 4, 3)
for k, curva in enumerate(curvas):
    xy = [f"({x:+.2f}, {y:+.2f})" for x, y, _ in curva]
    print(f"Curva {k}:", " ".join(xy))
print()
circulo = Circle(radius=1)
print("Circle: puntos =", len(circulo.points),
      "| curvas =", circulo.get_num_curves())
print("Anclas del círculo:", len(circulo.get_anchors()))
