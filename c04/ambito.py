# error-esperado: una variable local no existe fuera de su función
contador = 0                  # variable global


def incrementar():
    contador = 10             # otra variable, local a la función
    print("dentro:", contador)


incrementar()
print("fuera:", contador)


def area(radio):
    resultado = 3.14159 * radio ** 2
    return resultado


print(area(1))
print(resultado)
