from manim import *

# Ejercicio 32.13: copia de proyecto4/formato_vertical.py para 16:9.
# Mismos nombres (arriba, lineas, zona_segura y las constantes): la
# cápsula solo cambia la línea que importa el módulo de formato.
config.pixel_width, config.pixel_height = 1920, 1080
config.frame_width, config.frame_height = 16, 9

# Las plataformas horizontales tapan poco: márgenes menores
MARGEN_ARRIBA, MARGEN_ABAJO, MARGEN_LADOS = 0.7, 0.7, 0.8
TAM_GANCHO, TAM_TEXTO = 64, 44


def zona_segura():
    """Rectángulo de diseño: lo importante debe quedar dentro."""
    alto = config.frame_height - MARGEN_ARRIBA - MARGEN_ABAJO
    ancho = config.frame_width - 2 * MARGEN_LADOS
    return DashedVMobject(
        Rectangle(width=ancho, height=alto).shift(
            UP * (MARGEN_ABAJO - MARGEN_ARRIBA) / 2
        ),
        num_dashes=60,
    )


def arriba(mob, extra=0):
    """Coloca un objeto justo bajo el margen superior seguro."""
    return mob.to_edge(UP, buff=MARGEN_ARRIBA + extra)


def lineas(*textos, tam=TAM_TEXTO):
    """Varias líneas de texto, centradas."""
    return VGroup(
        *[Text(t, font_size=tam) for t in textos]
    ).arrange(DOWN, buff=0.25)
