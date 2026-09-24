# Guion de la lección «La suma de los impares es un cuadrado».
# Es un módulo de datos: lo importan el programa de tiempos, el de
# subtítulos y la escena de Manim: el guion se escribe una sola vez.

GUION = [
    {"bloque": "gancho",
     "voz": "Suma uno más tres más cinco más siete. "
            "¿Te sale dieciséis? Prueba con los cinco primeros impares.",
     "video": "Aparece la suma 1 + 3 + 5 + 7 = ? con la interrogación."},
    {"bloque": "pregunta",
     "voz": "Siempre sale un número al cuadrado. ¿Casualidad, "
            "o hay una razón que se pueda ver?",
     "video": "Lista 1, 4, 9, 16, 25; se resaltan como cuadrados."},
    {"bloque": "construccion",
     "voz": "Dibuja cada impar como una escuadra de puntos. El uno es un "
            "punto; el tres, una escuadra que lo abraza; el cinco, otra "
            "más grande. Cada escuadra completa un cuadrado mayor.",
     "video": "Las escuadras de 1, 3, 5 y 7 puntos encajan una a una."},
    {"bloque": "generalizacion",
     "voz": "Con n escuadras se forma un cuadrado de lado n. Por eso la "
            "suma de los n primeros impares es n al cuadrado.",
     "video": "Se escribe 1 + 3 + ... + (2n - 1) = n^2 bajo la figura."},
    {"bloque": "cierre",
     "voz": "La próxima vez que sumes impares, piensa en escuadras. "
            "¿Qué figura esconderá la suma de los números pares?",
     "video": "Fórmula enmarcada; pregunta final en pantalla."},
]

PALABRAS_POR_MINUTO = 150  # mide tu propia lectura y ajusta este valor


def duracion(bloque, ppm=PALABRAS_POR_MINUTO, respiro=1.0):
    """Segundos de narración de un bloque más un respiro final."""
    return len(bloque["voz"].split()) / ppm * 60 + respiro
