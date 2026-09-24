# Tuplas: secuencias que no se pueden modificar
punto = (2, 3)
print(punto[0], punto[1])
x, y = punto              # desempaquetar
print(f"x = {x}, y = {y}")
a, b = 1, 2
a, b = b, a               # intercambio en una línea
print(a, b)
vertices = [(0, 0), (4, 0), (0, 3)]   # lista de tuplas
for vx, vy in vertices:
    print(f"vértice ({vx}, {vy})")
print(len(vertices), vertices[1])
