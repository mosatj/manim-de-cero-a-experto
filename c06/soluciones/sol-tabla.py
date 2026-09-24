import numpy as np

x = np.linspace(-1, 3, 9)
y = x**2 - 2 * x                   # toda la tabla de una vez
for xi, yi in zip(x, y):
    print(f"x = {xi:5.2f}   f(x) = {yi:5.2f}")
i = y.argmin()
print("mínimo de la tabla:", y[i], "en x =", x[i])
