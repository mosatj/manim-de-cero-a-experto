# error-esperado: un argumento por nombre que la función no conoce
def describir_circulo(radio=1.0, color="BLANCO", relleno=0.0):
    print(f"radio={radio} color={color} relleno={relleno}")


describir_circulo(radius=2)
