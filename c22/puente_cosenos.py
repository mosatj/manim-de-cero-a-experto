import math

# Datos del puente (tesis de Chacón y Fernández, 2024)
b, a = 6.71, 7.21                  # AC y BC, en km
C = math.radians(39.5)             # ángulo en C
c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(C))
print(f"AB = c = {c:.2f} km")
# Con los tres lados, los otros dos ángulos (otra vez la ley)
A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
print(f"A = {A:.2f}°, B = {B:.2f}°, suma = {A + B + 39.5:.2f}°")
