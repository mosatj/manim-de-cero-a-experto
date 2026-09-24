# Propuesto: Fibonacci y la razón áurea
a, b = 0, 1
terminos = []
while len(terminos) < 15:
    terminos.append(a)
    a, b = b, a + b
print(terminos)
for k in range(10, 15):
    razon = terminos[k] / terminos[k - 1]
    print(f"F{k}/F{k-1} = {razon:.6f}")
