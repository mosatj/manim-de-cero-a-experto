# Comprensiones: construir listas en una sola línea
cuadrados = [k ** 2 for k in range(1, 8)]
print(cuadrados)
pares = [k for k in range(20) if k % 2 == 0]
print(pares)
puntos = [(x, x ** 2) for x in range(-2, 3)]
print(puntos)
# lo mismo que la primera línea, escrito con un bucle:
cuadrados2 = []
for k in range(1, 8):
    cuadrados2.append(k ** 2)
print(cuadrados == cuadrados2)
etiquetas = {k: f"P{k}" for k in range(3)}
print(etiquetas)
