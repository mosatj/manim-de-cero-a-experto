from manim import *

escena = Scene()
a, b, c = Square(), Circle(), Triangle()
grupo = VGroup(b, c)
escena.add(a, grupo)
print("mobjects:", escena.mobjects)
escena.add(a)            # añadir de nuevo lo lleva al final
print("mobjects:", escena.mobjects)
escena.remove(b)         # quitar un hijo desarma su grupo
print("mobjects:", escena.mobjects)
