# Funciones que fabrican funciones, y una trampa con los bucles
def multiplicador(k):
    def por_k(x):
        return k * x          # por_k «recuerda» el valor de k
    return por_k


triple = multiplicador(3)
print(triple(5), multiplicador(10)(5))

tardias = [lambda x: i * x for i in range(3)]
print([f(10) for f in tardias])       # todas usan el último i

fijadas = [lambda x, i=i: i * x for i in range(3)]
print([f(10) for f in fijadas])       # cada una guarda su i
