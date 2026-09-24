# Azar reproducible con el módulo random y una semilla
import random

random.seed(2026)             # fija el punto de partida
print(random.random())                        # en [0, 1)
print(random.randint(1, 6), random.uniform(-1, 1))
colores = ["rojo", "verde", "azul", "amarillo"]
print(random.choice(colores), random.sample(colores, 2))
cartas = list(range(1, 9))
random.shuffle(cartas)                        # baraja la lista
print(cartas)

random.seed(2026)             # la misma semilla...
print(random.random())        # ...repite la misma sucesión
