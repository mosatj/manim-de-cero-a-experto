import copy


class Punto:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Punto({self.x}, {self.y})"


a = Punto(1, 1)
b = a            # NO copia: b es otro nombre del mismo objeto
b.x = 99
print("a =", a, "| b =", b, "| ¿mismo objeto?", a is b)

c = copy.copy(a)           # ahora sí: un objeto nuevo con los datos
c.x = 0
print("a =", a, "| c =", c, "| ¿mismo objeto?", a is c)
