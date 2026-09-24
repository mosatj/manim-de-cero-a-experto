from manim import *


def cadena(clase):
    """Devuelve la herencia de una clase como texto."""
    nombres = [c.__name__ for c in clase.mro()]
    return " > ".join(nombres[:-1])  # sin 'object'


for clase in [Square, Triangle, Star, Arrow, Ellipse,
              VGroup, Group, MathTex, Text, ImageMobject]:
    print(f"{clase.__name__:>12}: {cadena(clase)}")
