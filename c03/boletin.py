# Boletín de un aula: promedio, aprobados y mejor nota
notas = {"Ana": 17, "Luis": 9, "Rosa": 14, "Iván": 10, "Sara": 19}
total = 0
aprobados = []
mejor, nota_mejor = "", -1
for alumno, nota in notas.items():
    total += nota
    if nota >= 11:
        aprobados.append(alumno)
    if nota > nota_mejor:        # ¿supera al mejor hasta ahora?
        mejor, nota_mejor = alumno, nota
promedio = total / len(notas)
print(f"Promedio del aula: {promedio:.1f}")
print(f"Aprobados ({len(aprobados)}): {', '.join(aprobados)}")
print(f"Mejor nota: {mejor} con {nota_mejor}")
for alumno in sorted(notas):
    barra = "#" * notas[alumno]
    print(f"{alumno:<5} {notas[alumno]:>2} {barra}")
