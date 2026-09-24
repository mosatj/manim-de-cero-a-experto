# Propuesto: números primos hasta 50
primos = []
for n in range(2, 51):
    es_primo = True
    for d in range(2, n):
        if d * d > n:
            break            # basta probar divisores hasta la raíz
        if n % d == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(n)
print(primos)
print("Hay", len(primos), "primos menores o iguales que 50")
