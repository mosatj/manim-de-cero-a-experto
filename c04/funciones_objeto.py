# Las funciones también son objetos: se guardan y se pasan
def cuadrado(x):
    return x * x


def cubo(x):
    return x ** 3


f = cuadrado                 # sin paréntesis: la función misma
print(f(4), f.__name__)


def aplicar(funcion, valores):
    return [funcion(v) for v in valores]


print(aplicar(cuadrado, [1, 2, 3]))
print(aplicar(cubo, [1, 2, 3]))
for g in [cuadrado, cubo, abs]:
    print(g.__name__, g(-2))
