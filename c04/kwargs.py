# **kwargs: cualquier cantidad de argumentos por nombre
def estilo(nombre, **opciones):
    print(f"{nombre}: {opciones}")      # llegan como un diccionario


estilo("círculo", color="ROJO", radio=2)
estilo("texto")
config = {"color": "AZUL", "grosor": 4}
estilo("línea", **config)    # el ** desempaqueta el diccionario
