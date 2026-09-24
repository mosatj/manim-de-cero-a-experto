class Circulo:
    pi = 3.14159          # atributo de CLASE: compartido por todos
    creados = 0           # cuántos círculos se han creado

    def __init__(self, radio):
        self.radio = radio             # atributo de INSTANCIA
        Circulo.creados += 1

    def area(self):
        return self.pi * self.radio**2  # self.pi busca en la clase


a, b = Circulo(1), Circulo(10)
print("creados:", Circulo.creados, "| a.pi:", a.pi, "| b.pi:", b.pi)
a.pi = 3        # atributo de instancia que TAPA al de la clase
print("a.area() =", a.area(), "| b.area() =", b.area())
print("a.__dict__ =", a.__dict__, "| b.__dict__ =", b.__dict__)
