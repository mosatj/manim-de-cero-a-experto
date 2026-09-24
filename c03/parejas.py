# enumerate da (índice, valor); zip recorre en paralelo
colores = ["rojo", "verde", "azul"]
for i, color in enumerate(colores):
    print(i, color)
radios = [0.5, 1.0, 1.5]
for color, radio in zip(colores, radios):
    print(f"círculo {color} de radio {radio}")
print(list(zip(colores, radios)))
