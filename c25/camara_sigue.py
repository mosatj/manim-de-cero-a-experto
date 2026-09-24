from manim import *


class CamaraSigue(MovingCameraScene):
    def construct(self):
        marco = self.camera.frame
        ejes = Axes(x_range=[0, 4 * PI, PI], y_range=[-1.5, 1.5],
                    x_length=12, y_length=4)
        curva = ejes.plot(np.sin, x_range=[0, 4 * PI], color=BLUE)
        movil = Dot(curva.get_start(), color=ORANGE)
        self.add(ejes, curva, movil)

        marco.save_state()
        self.play(marco.animate.scale(0.4).move_to(movil))
        # El marco debe estar en la escena para que su updater corra
        self.add(marco)
        marco.add_updater(lambda m: m.move_to(movil))
        self.play(MoveAlongPath(movil, curva), run_time=5,
                  rate_func=linear)
        marco.clear_updaters()            # soltar la cámara
        self.play(Restore(marco))
