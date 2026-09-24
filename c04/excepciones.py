# try/except: seguir adelante aunque un dato esté mal
datos = ["3.5", "2", "dos", "", "7.25"]
numeros = []
for texto in datos:
    try:
        numeros.append(float(texto))
    except ValueError:
        print(f"Ignoro {texto!r}: no es un número")
print(numeros)
