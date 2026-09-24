import numpy as np

x = np.linspace(0, 1, 5)       # 5 valores de 0 a 1, ambos incluidos
print("linspace:", x)
print("arange  :", np.arange(0, 10, 2.5))  # paso 2.5, sin el 10
paso = np.arange(0, 1, 0.1)
print("arange(0, 1, 0.1):", len(paso), "valores; último:", paso[-1])
print("¿0.1 + 0.2 == 0.3?", 0.1 + 0.2 == 0.3, "| isclose:",
      np.isclose(0.1 + 0.2, 0.3))

t = np.linspace(0, np.pi, 5)
y = np.sin(t)              # función vectorizada: seno de cada valor
print("sin(t):", np.round(y, 3))
print("máscara y > 0.5:", y > 0.5, "->", np.round(y[y > 0.5], 3))
print("suma:", round(y.sum(), 3), "| media:", round(y.mean(), 3),
      "| máximo en el índice", y.argmax())
print("acumulada:", np.cumsum([1, 2, 3, 4]))
