import csv
import statistics as st
import numpy as np

# 1) Con el módulo csv de la biblioteca estándar
with open("datos/estudio.csv", encoding="utf-8") as f:
    filas = list(csv.DictReader(f))   # una fila = un diccionario
print(filas[0])                       # ¡los valores son texto!
horas = [float(fila["horas"]) for fila in filas]
notas = [float(fila["nota"]) for fila in filas]
print(f"n = {len(notas)}, media = {st.mean(notas):.2f}, "
      f"desviación = {st.stdev(notas):.2f}")

# 2) Con NumPy: una matriz de números en una sola línea
datos = np.loadtxt("datos/estudio.csv", delimiter=",",
                   skiprows=1)
x, y = datos[:, 0], datos[:, 1]
print("forma:", datos.shape)

# Recta de mínimos cuadrados y = m x + b, y correlación r
dx, dy = x - x.mean(), y - y.mean()
m = (dx * dy).sum() / (dx ** 2).sum()
b = y.mean() - m * x.mean()
r = np.corrcoef(x, y)[0, 1]
print(f"m = {m:.3f}, b = {b:.3f}, r = {r:.3f}")
print("polyfit:", np.polyfit(x, y, 1).round(3))  # comprobación
