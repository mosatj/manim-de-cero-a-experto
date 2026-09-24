# if / elif / else: elegir el color según el signo
for valor in [-2.5, 0, 3]:
    if valor > 0:
        color = "azul"
    elif valor < 0:
        color = "rojo"
    else:
        color = "blanco"
    print(f"{valor:>5} se pinta de {color}")
