# Avisa si dos colores de una paleta se confunden en gris


def luminancia(hexa):
    c = [int(hexa[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
         for v in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def revisar(paleta, umbral=1.5):
    nombres = list(paleta)
    for i, a in enumerate(nombres):
        for b in nombres[i + 1:]:
            la, lb = sorted([luminancia(paleta[a]),
                             luminancia(paleta[b])])
            razon = (lb + 0.05) / (la + 0.05)
            marca = "  <-- se confunden" if razon < umbral else ""
            print(f"{a:>8} / {b:<8} {razon:4.2f}:1{marca}")


revisar({"RED": "#FC6255", "GREEN": "#83C167", "BLUE": "#58C4DD",
         "YELLOW": "#F7D96F"})
