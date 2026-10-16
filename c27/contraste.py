# Razón de contraste de las pautas WCAG entre un color y el fondo.
# Los valores hexadecimales son los de las constantes de Manim.

COLORES = {
    "WHITE": "#FFFFFF", "YELLOW": "#F7D96F", "BLUE": "#58C4DD",
    "GREEN": "#83C167", "RED": "#FC6255", "PURPLE": "#9A72AC",
    "GRAY": "#888888", "BLUE_E": "#236B8E", "PURE_BLUE": "#0000FF",
    "DARK_GRAY": "#444444",
}


def luminancia(hexa):
    """Luminancia relativa (0 = negro, 1 = blanco)."""
    canales = [int(hexa[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    lineal = [c / 12.92 if c <= 0.04045
              else ((c + 0.055) / 1.055) ** 2.4 for c in canales]
    r, g, b = lineal
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contraste(hexa1, hexa2):
    l1, l2 = sorted([luminancia(hexa1), luminancia(hexa2)])[::-1]
    return (l1 + 0.05) / (l2 + 0.05)


print(f"{'color':<10} {'s/ negro':>9} {'s/ blanco':>10}  veredicto")
for nombre, hexa in COLORES.items():
    negro = contraste(hexa, "#000000")
    blanco = contraste(hexa, "#FFFFFF")
    veredicto = "texto OK" if negro >= 4.5 else (
        "solo trazos gruesos" if negro >= 3 else "evitar sobre negro")
    print(f"{nombre:<10} {negro:>8.1f}:1 {blanco:>8.1f}:1  {veredicto}")
