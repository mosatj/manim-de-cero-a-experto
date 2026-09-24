from manim import *

cuadrado = Square()
constructor = cuadrado.animate.rotate(TAU)
inicio = cuadrado.points
final = cuadrado.target.points
print("¿Mismos puntos al inicio y al final?",
      np.allclose(inicio, final))
# Transform interpola punto a punto: sin diferencia, no hay
# movimiento. Rotate, en cambio, gira ángulo a ángulo:
anim = Rotate(cuadrado, angle=TAU)
anim.begin()
anim.interpolate(0.5)
print("Rotate a mitad: ¿igual al inicio?",
      np.allclose(anim.mobject.points, inicio))
