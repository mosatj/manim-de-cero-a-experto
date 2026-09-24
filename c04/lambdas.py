# lambda: funciones pequeñas y anónimas, en una línea
doble = lambda x: 2 * x
print(doble(5))
print(list(map(lambda x: x ** 2, range(6))))
print(list(filter(lambda n: n % 3 == 0, range(15))))

palabras = ["Manim", "es", "una", "biblioteca", "Animada"]
print(sorted(palabras))                   # mayúsculas primero
print(sorted(palabras, key=str.lower))    # sin distinguir
print(sorted(palabras, key=len))          # por longitud

alumnos = [("Ana", 17), ("Luis", 9), ("Rosa", 14)]
print(sorted(alumnos, key=lambda a: a[1], reverse=True))
print(max(alumnos, key=lambda a: a[1]))
