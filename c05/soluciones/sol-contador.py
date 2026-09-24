class Ficha:
    total = 0                        # atributo de clase

    def __init__(self, color):
        Ficha.total += 1             # se modifica en la CLASE
        self.numero = Ficha.total    # atributo de instancia
        self.color = color

    def __repr__(self):
        return f"Ficha #{self.numero} ({self.color})"


fichas = [Ficha(c) for c in ["roja", "azul", "roja", "verde"]]
print(fichas)
print("creadas:", Ficha.total, "| vista desde un objeto:",
      fichas[0].total)
