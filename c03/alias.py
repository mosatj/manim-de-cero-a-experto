# Dos nombres, una misma lista
a = [1, 2, 3]
b = a            # b NO es una copia: es otro nombre
b.append(4)
print("a =", a)
print(a is b)

c = a.copy()     # ahora sí, una copia independiente
c.append(5)
print("a =", a, " c =", c)
print(a is c, a == c[:4])
