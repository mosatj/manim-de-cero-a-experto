class GrupoMal:
    miembros = []           # ¡una sola lista para TODOS los grupos!

    def agregar(self, cosa):
        self.miembros.append(cosa)


class GrupoBien:
    def __init__(self):
        self.miembros = []     # cada grupo estrena su propia lista

    def agregar(self, cosa):
        self.miembros.append(cosa)


g1, g2 = GrupoMal(), GrupoMal()
g1.agregar("círculo")
print("GrupoMal  -> g2.miembros =", g2.miembros)
h1, h2 = GrupoBien(), GrupoBien()
h1.agregar("círculo")
print("GrupoBien -> h2.miembros =", h2.miembros)
