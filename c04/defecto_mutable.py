# La trampa del valor por defecto mutable
def agregar(punto, lista=[]):        # ¡la lista se crea UNA vez!
    lista.append(punto)
    return lista


print(agregar(1))
print(agregar(2))                     # sorpresa: arrastra el 1


def agregar_bien(punto, lista=None):
    if lista is None:
        lista = []                # una lista nueva en cada llamada
    lista.append(punto)
    return lista


print(agregar_bien(1))
print(agregar_bien(2))
