from manim import *
from congelar import congelar


class AlfaCreate(Scene):
    def construct(self):
        alfas = [0.2, 0.4, 0.6, 0.8, 1.0]
        for i, alfa in enumerate(alfas):
            centro = np.array([-5.6 + 2.8 * i, 0.6, 0])
            estrella = Star(outer_radius=1.1, color=YELLOW)
            estrella.move_to(centro)
            # Detenemos Create(estrella) en el instante alfa
            congelar(self, Create(estrella), alfa)
            tiempo = MathTex(rf"\alpha = {alfa}", font_size=40)
            avance = MathTex(
                rf"\text{{avance}} = {smooth(alfa):.2f}",
                font_size=30, color=GRAY_B,
            )
            tiempo.move_to(centro + 1.8 * DOWN)
            avance.next_to(tiempo, DOWN, buff=0.25)
            self.add(tiempo, avance)
