from manim import *


class RotuloFijo(MovingCameraScene):
    def construct(self):
        marco = self.camera.frame
        ancho0 = marco.width              # ancho del plano general
        figuras = VGroup(Circle(color=BLUE), Square(color=GREEN),
                         Triangle(color=RED)).arrange(RIGHT, buff=4)
        self.add(figuras)

        titulo = Text("Tres figuras", font_size=36)
        hueco = np.array([2.3, -0.5, 0])  # desde la esquina UL

        def pegar_al_marco(m):
            # Escala y posición proporcionales al marco
            m.set(width=marco.width * 0.28)
            escala = marco.width / ancho0
            m.move_to(marco.get_corner(UL) + escala * hueco)

        titulo.add_updater(pegar_al_marco)
        self.add(marco, titulo)
        for figura in figuras:
            self.play(marco.animate.set(width=5).move_to(figura),
                      run_time=1.5)
        self.play(marco.animate.set(width=ancho0).move_to(ORIGIN))
