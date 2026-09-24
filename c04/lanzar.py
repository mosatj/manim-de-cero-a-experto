# error-esperado: raise lanza una excepción propia
def circulo_seguro(radio):
    if radio <= 0:
        raise ValueError(f"el radio debe ser positivo, no {radio}")
    return f"círculo de radio {radio}"


print(circulo_seguro(2))
try:
    circulo_seguro(-1)
except ValueError as error:
    print("Capturado:", error)
circulo_seguro(0)             # sin try: detiene el programa
