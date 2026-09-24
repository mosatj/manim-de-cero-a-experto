import numpy as np

malo = np.arange(0, 1.1, 0.1)       # funciona... por casualidad
print(len(malo), malo[-1])
print(np.arange(1, 1.3, 0.1), "¡incluye 1.3!")
bueno = np.linspace(0, 1, 11)       # 11 valores, 0 y 1 incluidos
print(bueno)
print("¿el último es exactamente 1?", bueno[-1] == 1.0)
