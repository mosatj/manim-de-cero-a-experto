# Paradigma orientado a objetos: cada círculo sabe calcular su área
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio**2


circulos = [Circulo(1), Circulo(2), Circulo(3)]
for c in circulos:
    print(f"círculo de radio {c.radio}: área {c.area():.2f}")
print(f"área total: {sum(c.area() for c in circulos):.2f}")
