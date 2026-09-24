# Una lambda creada en un bucle recuerda la VARIABLE, no su valor
desplazamientos = [lambda: 0.5 * k for k in range(4)]
print([f() for f in desplazamientos])      # ¡todas valen lo último!

# Solución: congelar el valor con un argumento por defecto
desplazamientos = [lambda k=k: 0.5 * k for k in range(4)]
print([f() for f in desplazamientos])

# Lo mismo con un actualizador de Manim:
#   punto.add_updater(lambda m, k=k: m.move_to(ejes.c2p(k, f(k))))
