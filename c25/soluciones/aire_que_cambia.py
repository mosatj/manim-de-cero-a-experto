from manim import *


class AireQueCambia(MovingCameraScene):
    def construct(self):
        marco = self.camera.frame
        plano = NumberPlane(x_range=[-4, 22, 1], y_range=[-5, 5, 1])
        plano.background_lines.set_stroke(opacity=0.5)
        x = ValueTracker(0)
        punto = always_redraw(lambda: Dot(
            plano.c2p(x.get_value(), 0), radius=0.14, color=RED))
        marco.set(width=9).move_to(punto)
        estado = {"previa": 0.0, "aire": 0.0}

        def seguir(m, dt):
            if dt == 0:                   # fotograma sin tiempo
                return
            actual = punto.get_x()
            v = (actual - estado["previa"]) / dt
            estado["previa"] = actual
            # Aire deseado: un sexto del ancho hacia donde va
            deseado = np.sign(v) * m.width / 6
            k = 1 - np.exp(-2.5 * dt)     # suavizado (Steadicam)
            estado["aire"] += (deseado - estado["aire"]) * k
            m.move_to([actual + estado["aire"], 0, 0])

        self.add(plano, punto, marco)
        marco.add_updater(seguir)
        self.play(x.animate.set_value(12), run_time=5,
                  rate_func=linear)
        self.play(x.animate.set_value(4), run_time=4,
                  rate_func=linear)
