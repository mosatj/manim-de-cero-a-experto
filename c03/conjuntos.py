# Conjuntos: sin orden y sin repetidos
colores = ["rojo", "azul", "rojo", "verde", "azul"]
distintos = set(colores)
print(len(colores), len(distintos), sorted(distintos))
pares = {0, 2, 4, 6, 8}
primos = {2, 3, 5, 7}
print(pares & primos, primos - pares)   # intersección, diferencia
print(sorted(pares | primos))           # unión
