# Devolver varios valores, salir antes y el valor None
def cociente_y_resto(a, b):
    return a // b, a % b          # devuelve una tupla


def signo(x):
    if x > 0:
        return "positivo"         # return termina la función
    if x < 0:
        return "negativo"
    return "cero"


def sin_return():
    pass                          # «no hacer nada»


q, r = cociente_y_resto(17, 5)
print(q, r)
print(signo(-3), signo(0), signo(2.5))
print(sin_return())
