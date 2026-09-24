# Propuesto: el programa con errores, ya corregido
lados = [3, 4, 5]
perimetro = 0
for lado in lados:
    perimetro = perimetro + lado
if perimetro > 10:
    print("Perímetro grande: " + str(perimetro))
print("Último lado:", lados[2])
