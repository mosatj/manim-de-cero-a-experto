from manim import *

cara = Circle(radius=2)
ojos = VGroup(Dot(LEFT * 0.7 + UP * 0.5),
              Dot(RIGHT * 0.7 + UP * 0.5))
boca = Arc(radius=1, start_angle=PI * 1.2, angle=PI * 0.6)
emoticono = VGroup(cara, ojos, boca)

print("Hijos directos:", len(emoticono.submobjects))
print("Familia completa:", len(emoticono.get_family()))
for m in emoticono.get_family():
    print("   ", type(m).__name__, "| puntos:", len(m.points))
con_puntos = emoticono.family_members_with_points()
print("Con puntos:", len(con_puntos))
print()
palabra = Text("Hola mundo")
print("len(Text('Hola mundo')) =", len(palabra))
print("Primer hijo:", type(palabra[0]).__name__)
