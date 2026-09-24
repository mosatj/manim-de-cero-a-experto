# Paradigma imperativo: una receta de pasos que cambian variables
radios = [1, 2, 3]
total = 0
for r in radios:
    area = 3.14159 * r**2
    print(f"círculo de radio {r}: área {area:.2f}")
    total = total + area
print(f"área total: {total:.2f}")
