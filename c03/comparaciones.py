# Comparaciones y operadores lógicos: el resultado es un bool
x = 3
print(x > 2, x == 3, x != 3, 1 <= x <= 5)
print(x > 0 and x % 2 == 0)    # ¿positivo Y par?
print(x > 0 or x % 2 == 0)     # ¿positivo O par?
print(not x > 0, "a" == "A")
