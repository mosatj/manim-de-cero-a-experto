from manim import *
from rotacion import rotacion       # nuestra función (rotacion.py)

mia = rotacion(PI / 6)
de_manim = rotation_matrix(PI / 6, OUT)   # eje OUT = eje z
print("¿iguales?", np.allclose(mia, de_manim))
girado = rotate_vector(RIGHT, PI / 2)     # gira un vector suelto
print("rotate_vector(RIGHT, 90°) =", np.round(girado, 3))
