# *args: cualquier cantidad de argumentos posicionales
def sumar(*numeros):
    print("  numeros =", numeros)       # llegan como una tupla
    return sum(numeros)


print(sumar(1, 2))
print(sumar(1, 2, 3, 4))
print(sumar())
valores = [10, 20, 30]
print(sumar(*valores))      # el * desempaqueta la lista al llamar
