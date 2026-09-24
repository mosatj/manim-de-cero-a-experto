from manim import *

hojas = [Dot() for _ in range(4)]
interno = VGroup(hojas[0], hojas[1])
medio = VGroup(interno, hojas[2])
externo = VGroup(medio, hojas[3], Square())

print("Hijos directos:", len(externo.submobjects))
print("Familia:", len(externo.get_family()))
con_puntos = externo.family_members_with_points()
print("Con puntos:", len(con_puntos))
