class Circulo:
    def __init__(self, radio):
        self.radio = radio          # pasa por el «setter» de abajo

    @property
    def radio(self):            # se lee como un atributo: c.radio
        return self._radio

    @radio.setter
    def radio(self, valor):     # se ejecuta en: c.radio = valor
        if valor <= 0:
            raise ValueError(f"radio inválido: {valor}")
        self._radio = valor

    @property
    def area(self):             # propiedad calculada, sin setter
        return 3.14159 * self._radio**2


c = Circulo(2)
print("radio:", c.radio, "| área:", c.area)
c.radio = 3
print("radio:", c.radio, "| área:", round(c.area, 3))
try:
    c.radio = -1
except ValueError as error:
    print("Error atrapado:", error)
