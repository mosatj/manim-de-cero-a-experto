from manim import *
from componentes import Balanza


def pesa(texto, color):
    caja = Square(side_length=0.8, color=color, fill_opacity=0.5)
    return VGroup(caja, MathTex(texto, font_size=36).move_to(caja))


class BalanzaEscena(Scene):
    def construct(self):
        balanza = Balanza(largo=7).scale(1.3).shift(DOWN)
        self.add(balanza)
        balanza.poner(0, pesa("x", GOLD)).poner(0, pesa("2", BLUE))
        balanza.poner(1, pesa("5", BLUE))
        self.play(FadeIn(balanza.cargas))
        # Si x fuese 1, el lado izquierdo pesaría menos (3 < 5)
        self.play(balanza.animar_inclinacion(-12 * DEGREES))
        self.play(balanza.animar_inclinacion(0))  # si x = 3
        self.wait()
