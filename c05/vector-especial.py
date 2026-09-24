import math


class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):                  # para programadores
        return f"Vector({self.x}, {self.y})"

    def __str__(self):                   # para personas (print)
        return f"⟨{self.x}, {self.y}⟩"

    def __add__(self, otro):             # v + w
        return Vector(self.x + otro.x, self.y + otro.y)

    def __mul__(self, k):                # v * 3
        return Vector(k * self.x, k * self.y)

    def __rmul__(self, k):               # 3 * v (k a la izquierda)
        return self * k

    def __abs__(self):                   # abs(v): la longitud
        return math.hypot(self.x, self.y)

    def __eq__(self, otro):              # v == w
        return (self.x, self.y) == (otro.x, otro.y)


arriba, derecha = Vector(0, 1), Vector(1, 0)
v = 2 * arriba + derecha * 3
print(v)                     # usa __str__
print([v, arriba])           # dentro de una lista se usa __repr__
print(abs(Vector(3, 4)), v == Vector(3, 2))
