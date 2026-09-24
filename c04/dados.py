# Lanzar dos dados 3600 veces: ¿qué suma sale más?
import random


def lanzar_dados(veces, semilla=None):
    """Devuelve un diccionario {suma: frecuencia}."""
    generador = random.Random(semilla)     # un generador propio
    frecuencias = {suma: 0 for suma in range(2, 13)}
    for _ in range(veces):
        suma = generador.randint(1, 6) + generador.randint(1, 6)
        frecuencias[suma] += 1
    return frecuencias


conteo = lanzar_dados(3600, semilla=7)
for suma, veces in conteo.items():
    print(f"{suma:>2} {veces:>4} {'#' * (veces // 20)}")
print("¿Reproducible?", conteo == lanzar_dados(3600, semilla=7))
