# Propuesto: un diccionario de saludos y un valor por defecto
SALUDOS = {"es": "Hola", "en": "Hello", "pt": "Olá", "it": "Ciao"}


def saludo(nombre, idioma="es"):
    palabra = SALUDOS.get(idioma, SALUDOS["es"])
    return f"{palabra}, {nombre}"


print(saludo("Ada"))
print(saludo("Ada", "pt"))
print(saludo("Ada", idioma="en"))
print(saludo("Ada", "fr"))       # idioma desconocido: español
