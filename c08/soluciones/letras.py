from manim import *

for cadena in ["Manim", "Hola mundo", "a b c", "¡Sí!"]:
    print(f"{cadena!r:>13}: len = {len(Text(cadena))}")
