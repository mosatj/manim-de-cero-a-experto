# Paradigma funcional: se combinan funciones que no cambian nada
def area(r):
    return 3.14159 * r**2

radios = [1, 2, 3]
areas = list(map(area, radios))
print("áreas:", [round(a, 2) for a in areas])
print(f"área total: {sum(areas):.2f}")
