# Propuesto: suma de los múltiplos de 3 o de 5 menores que 100
total = 0
for n in range(1, 100):
    if n % 3 == 0 or n % 5 == 0:
        total += n
print("Con un bucle:", total)
print("Con una comprensión:",
      sum([n for n in range(100) if n % 3 == 0 or n % 5 == 0]))
