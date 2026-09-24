class Figura:
    def __init__(self):
        self.x, self.y, self.tam, self.color = 0, 0, 1, "blanco"

    def desplazar(self, dx, dy):
        self.x, self.y = self.x + dx, self.y + dy
        return self             # devolver self permite encadenar

    def escalar(self, k):
        self.tam = self.tam * k
        return self

    def pintar(self, color):
        self.color = color
        return self

    def __repr__(self):
        return (f"Figura en ({self.x}, {self.y}), "
                f"tam {self.tam}, {self.color}")


f = Figura().desplazar(0, 1).escalar(2).pintar("rojo")
print(f)
# Se lee de izquierda a derecha; cada método recibe el objeto
# que devolvió el anterior, que siempre es el mismo:
print(f.desplazar(1, 0) is f)
