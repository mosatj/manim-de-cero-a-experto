# Devolver no es lo mismo que imprimir
def area_que_imprime(radio):
    print(3.14159 * radio ** 2)


def area(radio):
    return 3.14159 * radio ** 2


a = area_que_imprime(2)    # muestra el valor, pero no lo entrega
b = area(2)                # entrega el valor y no muestra nada
print("a =", a)
print("b =", b)
print("El doble del área:", 2 * area(2))
