class Contador:
    def __init__(self):
        self.valor = 0

    def sumar(self, cuanto):
        print("  dentro de sumar, id(self) =", id(self) % 10_000)
        self.valor = self.valor + cuanto


c = Contador()
print("fuera, id(c) =", id(c) % 10_000)
c.sumar(5)                   # la forma habitual...
Contador.sumar(c, 2)         # ...es un atajo de esta otra
print("valor final:", c.valor)
