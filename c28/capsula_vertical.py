from manim import *
from impares import cuadrado_de_escuadras

# Formato vertical 9:16 para redes. El ancho lógico se fija en 8 unidades:
# 1080 px / 8 = 135 px por unidad, igual que en 16:9 (1920 / 14,22).
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 8
config.frame_height = 8 * 16 / 9  # 14,22 unidades


def zona_segura(arriba=1.6, abajo=2.6, lados=0.5):
    """Rectángulo libre de la interfaz de la aplicación (orientativo)."""
    ancho, alto = config.frame_width, config.frame_height
    zona = Rectangle(width=ancho - 2 * lados, height=alto - arriba - abajo)
    zona.shift((abajo - arriba) / 2 * UP)
    return zona.set_stroke(RED, width=3)


class CapsulaVertical(Scene):
    def componer(self):
        gancho = Text("¿Cuánto suman\nlos impares?", font_size=60,
                      line_spacing=0.9).to_edge(UP, buff=2.0)
        figura = cuadrado_de_escuadras(5, lado=0.8).shift(0.5 * UP)
        formula = MathTex(r"1+3+5+\cdots+(2n-1)", r"=n^2",
                          font_size=56).arrange(DOWN, buff=0.3)
        formula.next_to(figura, DOWN, buff=0.6)
        return gancho, figura, formula

    def construct(self):
        gancho, figura, formula = self.componer()
        self.play(Write(gancho))
        self.play(LaggedStart(*[FadeIn(e, shift=0.3 * UR) for e in figura],
                              lag_ratio=0.4))
        self.play(Write(formula))


class CapsulaVerticalGuias(CapsulaVertical):
    def construct(self):
        super().construct()  # la misma cápsula...
        self.add(zona_segura())  # ...con la zona segura superpuesta
