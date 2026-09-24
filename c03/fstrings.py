# f-strings: cadenas con valores incrustados
nombre = "círculo"
radio = 1.5
area = 3.14159 * radio ** 2
print(f"El {nombre} de radio {radio} tiene área {area}")
print(f"Área con dos decimales: {area:.2f}")
print(f"Cálculo dentro de las llaves: {2 * radio}")
for n in [1, 10, 100]:
    print(f"|{n:>5}|{n:<5}|{n:^5}|")   # derecha, izquierda, centro
print(f"Porcentaje: {0.4567:.1%}")
