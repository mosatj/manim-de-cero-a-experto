# Propuesto: leer puntos "x, y" sin detenerse por los errores
def leer_puntos(lineas):
    """Devuelve (puntos, errores) a partir de líneas "x, y"."""
    puntos, errores = [], []
    for numero, linea in enumerate(lineas, start=1):
        try:
            x, y = linea.split(",")
            puntos.append((float(x), float(y)))
        except ValueError:
            errores.append(numero)
    return puntos, errores


datos = ["0, 0", "1.5, 2", "tres, 4", "5", "2, -1", "1, 2, 3"]
puntos, errores = leer_puntos(datos)
print("Puntos:", puntos)
print("Líneas con error:", errores)
