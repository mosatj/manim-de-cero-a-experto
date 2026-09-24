import numpy as np

gen = np.random.default_rng(2026)          # generador con semilla
print("enteros de 1 a 6:", gen.integers(1, 7, size=8))
print("uniformes [0, 1):", gen.random(3).round(3))
print("normales (0, 1) :", gen.normal(0, 1, 3).round(3))
print("elección        :", gen.choice(["rojo", "azul", "verde"], 4))

# La misma semilla reproduce exactamente la misma secuencia
a = np.random.default_rng(7).random(3)
b = np.random.default_rng(7).random(3)
print("¿misma semilla, mismos números?", np.array_equal(a, b))

# Monte Carlo: fracción de puntos del cuadrado dentro del círculo
p = np.random.default_rng(1).uniform(-1, 1, size=(100_000, 2))
dentro = (p**2).sum(axis=1) <= 1
print("estimación de π:", 4 * dentro.mean())
