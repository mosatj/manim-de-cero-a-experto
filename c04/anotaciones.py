# Anotaciones de tipo: documentan, pero Python no las impone
def area_rectangulo(base: float, altura: float = 1.0) -> float:
    return base * altura


print(area_rectangulo(3, 2.5))
print(area_rectangulo("ab", 3))       # ¡funciona!: "ab" * 3
print(area_rectangulo.__annotations__)
