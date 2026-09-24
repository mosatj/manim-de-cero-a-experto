# Propuesto: imprimir las propiedades recibidas por nombre
def ficha(nombre, **propiedades):
    print(f"[{nombre}]")
    for clave in sorted(propiedades):
        print(f"  {clave:<10} {propiedades[clave]}")


ficha("círculo", radio=1.5, color="ROJO", relleno=0.4)
ficha("punto")
