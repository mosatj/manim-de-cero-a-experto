import math


class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, w):
        return Vector(self.x + w.x, self.y + w.y)

    def __sub__(self, w):                # v - w
        return Vector(self.x - w.x, self.y - w.y)

    def __neg__(self):                   # -v
        return Vector(-self.x, -self.y)

    def __mul__(self, k):
        return Vector(k * self.x, k * self.y)

    __rmul__ = __mul__

    def __matmul__(self, w):             # v @ w: producto escalar
        return self.x * w.x + self.y * w.y

    def __abs__(self):
        return math.hypot(self.x, self.y)


v, w = Vector(3, 4), Vector(4, -3)
print(v - w, -v, 2 * v, abs(v))
print("v @ w =", v @ w, "→ perpendiculares:", v @ w == 0)
