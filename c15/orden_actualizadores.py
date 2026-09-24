import manim as mn

# Cadena: tracker -> punto -> etiqueta (sin renderizar nada)
x = mn.ValueTracker(0)
punto = mn.Dot().add_updater(lambda m: m.set_x(x.get_value()))
etiqueta = mn.Dot().add_updater(lambda m: m.set_x(punto.get_x()))

def fotograma(orden):
    for m in orden:          # así recorre Scene.update_mobjects
        m.update(dt=1 / 30)  # la lista self.mobjects

x.set_value(1)
fotograma([etiqueta, punto])      # la etiqueta va primero: MAL
print("seguidor antes:", punto.get_x(), etiqueta.get_x())
x.set_value(2)
fotograma([punto, etiqueta])      # el líder va primero: BIEN
print("líder antes:   ", punto.get_x(), etiqueta.get_x())
