from manim import *


class Semaforo(Scene):
    def construct(self):
        colores = {"rojo": RED, "ambar": ORANGE, "verde": GREEN}
        luces = VDict({nombre: Circle(radius=0.6, color=c)
                       for nombre, c in colores.items()})
        luces.arrange(DOWN, buff=0.3)
        caja = SurroundingRectangle(luces, color=GRAY, buff=0.3,
                                    corner_radius=0.3)
        self.add(caja, luces)
        for n in ["verde", "ambar", "rojo"]:
            self.play(luces[n].animate.set_fill(colores[n], 1),
                      run_time=0.5)
            self.play(luces[n].animate.set_fill(opacity=0),
                      run_time=0.5)
        self.play(luces["rojo"].animate.set_fill(RED, opacity=1))
