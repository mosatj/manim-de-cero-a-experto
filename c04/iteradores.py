# itertools: combinar y repetir sin escribir bucles anidados
from itertools import (accumulate, combinations, cycle, islice,
                       permutations, product)

print(list(product([0, 1, 2], [0, 1])))      # rejilla 3 x 2
print(list(combinations("ABCD", 2)))          # pares sin orden
print(len(list(permutations(range(4)))))      # 4! ordenaciones
print(list(accumulate([1, 2, 3, 4, 5])))      # sumas parciales
colores = cycle(["rojo", "verde", "azul"])     # se repite sin fin
print(list(islice(colores, 7)))               # tomamos 7
