# El guion es un dato: la escena lo lee, no lo copia a mano.
# Cada entrada es (clave, texto que se dirá en voz alta).
GUION = [
    (
        "pregunta",
        "Todos repetimos a al cuadrado más b al cuadrado "
        "igual a c al cuadrado. Pero ¿por qué es cierto?",
    ),
    (
        "triangulo",
        "Toma un triángulo rectángulo de catetos a y b "
        "e hipotenusa c.",
    ),
    (
        "marco",
        "Coloca cuatro copias dentro de un cuadrado de lado "
        "a más b.",
    ),
    (
        "hueco_c",
        "El espacio que queda libre es un cuadrado de lado c.",
    ),
    (
        "mover",
        "Ahora desliza los triángulos sin cambiar su tamaño.",
    ),
    (
        "hueco_ab",
        "El espacio libre es ahora un cuadrado de lado a "
        "y otro de lado b.",
    ),
    (
        "conclusion",
        "Los triángulos ocupan lo mismo en ambos casos. "
        "Por tanto, c al cuadrado es a al cuadrado más b "
        "al cuadrado.",
    ),
]
PALABRAS_POR_MINUTO = 150  # ritmo pausado de una clase


def texto(clave):
    return dict(GUION)[clave]


def duracion(clave):
    """Segundos que tarda en decirse la línea, más un respiro."""
    palabras = len(texto(clave).split())
    return palabras / PALABRAS_POR_MINUTO * 60 + 0.4


if __name__ == "__main__":
    total = 0.0
    for clave, _ in GUION:
        total += duracion(clave)
        print(
            f"{clave:11s} {duracion(clave):5.1f} s   acumulado "
            f"{total:5.1f} s"
        )
