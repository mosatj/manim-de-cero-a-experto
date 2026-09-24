# Seguir la pista a los valores con print y f"{variable=}"
def promedio(valores):
    total = 0
    for v in valores:
        total += v
        print(f"  {v=} {total=}")      # rastro temporal
    return total / len(valores)


print(promedio([4, 8, 9]))
assert promedio([2, 4]) == 3, "el promedio de 2 y 4 debe ser 3"
print("La comprobación pasó")
