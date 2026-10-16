# El guion como datos: (clave, frase). Las escenas leen por clave.
PALABRAS_POR_MINUTO = 150
RESPIRO = 0.4  # segundos de silencio tras cada frase

FRASES = [
    ("gancho", "¿Qué tienen en común estas dos figuras?"),
    ("idea", "Las dos se construyen con la misma regla."),
    ("cierre", "Esa regla es lo único que hace falta recordar."),
]


def texto(clave):
    return dict(FRASES)[clave]


def duracion(clave):
    palabras = len(texto(clave).split())
    return palabras * 60 / PALABRAS_POR_MINUTO + RESPIRO


if __name__ == "__main__":
    total = 0
    for clave, frase in FRASES:
        total += duracion(clave)
        print(f"{clave:8}{duracion(clave):5.1f} s  {frase}")
    print(f"{'total':8}{total:5.1f} s")
