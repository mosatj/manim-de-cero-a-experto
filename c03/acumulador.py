# Patrón acumulador: 1 + 2 + ... + 10
total = 0
for k in range(1, 11):
    total = total + k       # también: total += k
print("Suma:", total)

producto = 1
for k in range(1, 6):
    producto *= k
print("5! =", producto)
