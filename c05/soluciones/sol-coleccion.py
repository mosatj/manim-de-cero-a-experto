class MiGrupo:
    def __init__(self, *elementos):
        self.elementos = list(elementos)

    def __len__(self):
        return len(self.elementos)

    def __getitem__(self, i):
        if isinstance(i, slice):       # una rebanada es OTRO grupo
            return MiGrupo(*self.elementos[i])
        return self.elementos[i]

    def __iter__(self):
        return iter(self.elementos)

    def __contains__(self, x):
        return x in self.elementos

    def __add__(self, otro):                 # g + h: grupo nuevo
        return MiGrupo(*self.elementos, *otro.elementos)

    def __iadd__(self, otro):                # g += h: modifica g
        self.elementos.extend(otro.elementos)
        return self

    def __repr__(self):
        return f"MiGrupo{tuple(self.elementos)}"


g = MiGrupo("círculo", "cuadrado", "triángulo")
h = MiGrupo("estrella")
print(g[1:], len(g + h), "estrella" in g)
alias = g
g += h
print(g, "| ¿el mismo objeto?", alias is g)
