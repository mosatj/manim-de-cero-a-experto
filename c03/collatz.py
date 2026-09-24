# Conjetura de Collatz: si n es par, n/2; si es impar, 3n + 1
n = 27
recorrido = [n]
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    recorrido.append(n)
print("Pasos hasta llegar a 1:", len(recorrido) - 1)
print("Valor máximo alcanzado:", max(recorrido))
print("Primeros diez:", recorrido[:10])
print("Últimos cinco:", recorrido[-5:])
