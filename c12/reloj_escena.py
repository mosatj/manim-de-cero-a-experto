from manim import *
from componentes import Reloj


class RelojEscena(Scene):
    def construct(self):
        reloj = Reloj(radio=2.5, horas=3, minutos=0)
        rotulo = Text("3:00").next_to(reloj, RIGHT, buff=1)
        VGroup(reloj, rotulo).center()
        self.add(reloj, rotulo)
        # El componente fabrica la animación; la escena la usa
        for h, m in [(3, 30), (4, 0), (4, 30)]:
            nuevo = Text(f"{h}:{m:02d}").move_to(rotulo)
            self.play(reloj.animar_hora(h, m),
                      Transform(rotulo, nuevo), run_time=2)
