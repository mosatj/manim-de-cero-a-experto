from manim import *

# Formato 9:16 para reels y shorts. Debe ejecutarse ANTES de
# crear la escena: por eso vive en un módulo que se importa
# al principio.
config.pixel_width, config.pixel_height = 1080, 1920
config.frame_width, config.frame_height = 9, 16

# Márgenes seguros: zonas que las aplicaciones tapan con botones
MARGEN_ARRIBA, MARGEN_ABAJO, MARGEN_LADOS = 1.6, 2.4, 0.6
TAM_GANCHO, TAM_TEXTO = 64, 48  # nada menor de 40 en un móvil


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
