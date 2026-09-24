# Propuesto: promedio de cualquier cantidad de números
def promedio(*numeros):
    if not numeros:
        raise ValueError("promedio() necesita al menos un número")
    return sum(numeros) / len(numeros)


print(promedio(4, 8, 9))
notas = [14, 17, 11, 20]
print(promedio(*notas))
try:
    promedio()
except ValueError as error:
    print("Error:", error)
