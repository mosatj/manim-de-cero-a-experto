# Propuesto: 1000 lanzamientos de moneda, reproducibles
import random


def lanzar_monedas(veces, semilla):
    generador = random.Random(semilla)
    caras = sum(generador.random() < 0.5 for _ in range(veces))
    return caras


caras = lanzar_monedas(1000, semilla=42)
print(f"Caras: {caras} de 1000 ({caras / 1000:.1%})")
print("Otra vez:", lanzar_monedas(1000, semilla=42))
print("Otra semilla:", lanzar_monedas(1000, semilla=1))
