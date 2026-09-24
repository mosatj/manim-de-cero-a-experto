# Propuesto: ordenar por nota descendente y, si empatan, por nombre
alumnos = [("Luis", 14), ("Ana", 17), ("Rosa", 14), ("Iván", 9),
           ("Sara", 17)]
ranking = sorted(alumnos, key=lambda a: (-a[1], a[0]))
for puesto, (nombre, nota) in enumerate(ranking, start=1):
    print(puesto, nombre, nota)
