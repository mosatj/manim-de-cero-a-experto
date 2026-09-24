# Rejilla de puntos enteros y cuáles caen dentro de un círculo
radio = 2.5
puntos = [(x, y) for y in range(-3, 4) for x in range(-5, 6)]
dentro = [(x, y) for (x, y) in puntos if x**2 + y**2 <= radio**2]
print("Puntos en la rejilla:", len(puntos))
print("Dentro del círculo:", len(dentro))
for y in range(3, -4, -1):     # de arriba abajo, como en pantalla
    fila = ""
    for x in range(-5, 6):
        fila += "o " if (x, y) in dentro else ". "
    print(fila)
