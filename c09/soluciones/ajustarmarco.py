from manim import *


def ajustar_al_marco(mob, margen=0.5):
    """Reduce mob solo si no cabe con ese margen; lo centra."""
    ancho_max = config.frame_width - 2 * margen
    alto_max = config.frame_height - 2 * margen
    factor = min(1, ancho_max / mob.width,
                 alto_max / mob.height)
    return mob.scale(factor).move_to(ORIGIN)


class AjustarMarco(Scene):
    def construct(self):
        gigante = Rectangle(width=30, height=6, color=BLUE,
                            fill_opacity=0.3)
        self.add(ajustar_al_marco(gigante))
        borde = Rectangle(width=config.frame_width - 1,
                          height=config.frame_height - 1,
                          color=GRAY)
        self.add(DashedVMobject(borde, num_dashes=70))
