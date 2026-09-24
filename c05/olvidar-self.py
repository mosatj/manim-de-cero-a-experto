# error-esperado: un método definido sin el parámetro self
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area():                     # ¡falta self!
        return 3.14159 * self.radio**2


c = Circulo(2)
print(c.area())
