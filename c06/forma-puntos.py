import numpy as np

# Cuatro vértices de un cuadrado: un arreglo de forma (4, 3)
x = np.array([-1, 1, 1, -1])
y = np.array([-1, -1, 1, 1])
puntos = np.column_stack([x, y, np.zeros(4)])
print(puntos, "\nforma:", puntos.shape)

# Difusión (broadcasting): (4, 3) + (3,) suma el vector a cada fila
desplazados = puntos + np.array([5, 0, 0])
print("primera fila desplazada:", desplazados[0])
print("columna de las x:", desplazados[:, 0])
centro = puntos.mean(axis=0)            # media de cada columna
print("centro:", centro)
print("escalado respecto al centro:\n", 2 * (puntos - centro))
