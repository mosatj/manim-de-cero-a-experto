# Propuesto: comprensión con condición
cuadrados = [k ** 2 for k in range(1, 21) if k % 2 == 0]
print(cuadrados)
print("Cantidad:", len(cuadrados), " Suma:", sum(cuadrados))
