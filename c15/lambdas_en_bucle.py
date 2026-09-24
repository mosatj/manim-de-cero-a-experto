from manim import *


class LambdasEnBucle(Scene):
    def construct(self):
        dy = ValueTracker(0)  # desplazamiento vertical
        rojos, verdes, rotulos = VGroup(), VGroup(), VGroup()
        for k in range(4):
            x = -4.5 + 3 * k
            rojo = Dot([x, 1.5, 0], color=RED)
            verde = Dot([x, -1.5, 0], color=GREEN)
            rojos.add(rojo)
            verdes.add(verde)
            # MAL: «rojo» se busca cuando la lambda se EJECUTA,
            # y para entonces es el último punto del bucle
            rotulos.add(Integer(k, color=RED).add_updater(
                lambda m: m.next_to(rojo, UP)))
            # BIEN: p=verde congela el valor de ESTA vuelta
            rotulos.add(Integer(k, color=GREEN).add_updater(
                lambda m, p=verde: m.next_to(p, UP)))

        rojos.add_updater(lambda g: g.set_y(1.5 + dy.get_value()))
        verdes.add_updater(lambda g: g.set_y(-1.5 + dy.get_value()))
        self.add(rojos, verdes, rotulos)
        self.play(dy.animate.set_value(0.8))
