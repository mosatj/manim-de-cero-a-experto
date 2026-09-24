from manim import *


class EtiquetaQuePersigue(Scene):
    def construct(self):
        punto = Dot(LEFT * 4 + DOWN, radius=0.12, color=YELLOW)
        etiqueta = MathTex("P", font_size=48).next_to(punto, UP)
        radio = Line(ORIGIN, punto.get_center(), color=BLUE)
        origen = Dot(ORIGIN, color=BLUE)

        # Un actualizador es una función que recibe el objeto
        # y lo deja «al día»; Manim la llama en cada fotograma.
        def seguir_al_punto(m):
            m.next_to(punto, UP)

        def unir_con_el_punto(m):
            m.put_start_and_end_on(ORIGIN, punto.get_center())

        etiqueta.add_updater(seguir_al_punto)
        radio.add_updater(unir_con_el_punto)
        self.add(radio, origen, punto, etiqueta)

        # Solo movemos el punto: los demás lo siguen solos
        self.play(punto.animate.move_to(LEFT * 1.5 + UP * 2.5))
        self.play(punto.animate.move_to(RIGHT * 4 + UP))
        self.play(punto.animate.move_to(RIGHT * 3 + DOWN * 2))
