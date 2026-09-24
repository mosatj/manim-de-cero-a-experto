# Operaciones frecuentes con listas
notas = [14, 9, 17, 11]
notas.insert(0, 20)       # inserta en la posición 0
ultima = notas.pop()      # quita y devuelve el último
notas.remove(9)           # quita el primer 9
print(ultima, notas)
print(sorted(notas), notas)   # sorted crea una lista nueva
notas.sort()                  # sort ordena la misma lista
print(notas)
print(17 in notas, sum(notas), min(notas), max(notas))
print([0] * 5, [1, 2] + [3])
