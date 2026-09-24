from manim import *


class Diana(VGroup):
    """Componente propio: anillos concéntricos alternos."""

    def __init__(self, anillos=4, radio=2.0, colores=(RED, WHITE),
                 **kwargs):
        super().__init__(**kwargs)       # que VGroup se prepare
        for k in range(anillos):         # del anillo mayor al menor
            r = radio * (anillos - k) / anillos
            self.add(Circle(radius=r, color=colores[k % 2],
                            fill_opacity=1, stroke_width=1))

    def resaltar_centro(self, color=YELLOW):
        self[-1].set_fill(color)         # el último es el centro
        return self                      # para poder encadenar


class EscenaDianas(Scene):
    def construct(self):
        d1 = Diana()
        d2 = Diana(6, colores=(BLUE, WHITE)).resaltar_centro()
        dianas = VGroup(d1, d2.scale(0.75)).arrange(RIGHT, buff=1.2)
        self.play(Create(d1), GrowFromCenter(d2))
        for d in dianas:
            texto = Text(f"len = {len(d)}", font_size=30)
            self.add(texto.next_to(d, DOWN))
        # .animate también sirve con métodos propios
        self.play(d1.animate.resaltar_centro(GREEN))
