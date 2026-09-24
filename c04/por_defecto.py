# Parámetros con valor por defecto y argumentos por nombre
def describir_circulo(radio=1.0, color="BLANCO", relleno=0.0):
    print(f"radio={radio} color={color} relleno={relleno}")


describir_circulo()
describir_circulo(2)
describir_circulo(color="ROJO")
describir_circulo(1.5, relleno=0.5, color="AZUL")
