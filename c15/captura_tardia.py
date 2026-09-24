# Tres funciones creadas en un bucle... ¿qué devuelve cada una?
funciones = []
for i in range(3):
    funciones.append(lambda: i)          # lee i cuando SE LLAMA
print([f() for f in funciones])

# Arreglo: un argumento por defecto se evalúa al CREAR la lambda
funciones = []
for i in range(3):
    funciones.append(lambda i=i: i)
print([f() for f in funciones])
