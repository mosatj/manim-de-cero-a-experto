# ¿Cuántos píxeles necesita una figura impresa a 300 ppp?
PULGADA_CM = 2.54
for nombre, ancho_cm in (
    ("una columna", 8.5),
    ("doble columna", 17.5),
):
    ancho_px = round(ancho_cm / PULGADA_CM * 300)
    alto_px = round(ancho_px * 9 / 16)  # proporción 16:9
    print(
        f"{nombre:14s}: {ancho_cm} cm -> {ancho_px} x {alto_px} px"
    )
    print(f"    manim -s -r {ancho_px},{alto_px} figura.py Figura")
