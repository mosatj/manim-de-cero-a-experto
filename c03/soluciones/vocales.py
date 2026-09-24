# Propuesto: contar vocales con un diccionario
frase = "Las matemáticas animadas se entienden mejor"
cuenta = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
equivalente = {"á": "a", "é": "e", "í": "i", "ó": "o",
               "ú": "u"}
for letra in frase.lower():
    letra = equivalente.get(letra, letra)   # quita la tilde
    if letra in cuenta:
        cuenta[letra] += 1
for vocal, veces in cuenta.items():
    print(vocal, veces)
print("Total:", sum(cuenta.values()))
