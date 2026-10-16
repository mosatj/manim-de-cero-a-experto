from manim import *


class AireDelante(MovingCameraScene):
    def construct(self):
        marco = self.camera.frame
        plano = NumberPlane(x_range=[-6, 36, 1], y_range=[-5, 5, 1])
        plano.background_lines.set_stroke(opacity=0.5)
        curva = plano.plot(lambda x: 1.3 * np.sin(0.9 * x),
                           x_range=[0, 34], color=BLUE)
        x = ValueTracker(1)        # abscisa del punto
        aire = ValueTracker(0)     # adelanto del marco
        mezcla = ValueTracker(0)   # 0: sin aire; 1: con aire
        punto = always_redraw(lambda: Dot(
            plano.i2gp(x.get_value(), curva), radius=0.14,
            color=RED))
        marco.set(width=9).move_to([x.get_value(), 0, 0])

        def seguir(m):
            # Solo en horizontal: el punto sube y baja en el cuadro
            m.move_to([punto.get_x() + aire.get_value(), 0, 0])

        tercios = VGroup(*[DashedLine(UP, DOWN, color=GREY_B)
                           for _ in range(2)])
        sin_aire = Text("Sin aire", font_size=40)
        con_aire = Text("Con aire", font_size=40)

        def pegar(m):
            # Guías de tercios y rótulos, relativos al marco
            a, h = m.width, m.height
            for k, linea in enumerate(tercios, 1):
                x_k = m.get_left() + a * k / 3 * RIGHT
                linea.put_start_and_end_on(x_k + h / 2 * UP,
                                           x_k + h / 2 * DOWN)
            for rotulo, op in ((sin_aire, 1 - mezcla.get_value()),
                               (con_aire, mezcla.get_value())):
                rotulo.set(width=a * 0.3).set_opacity(op)
                rotulo.move_to(m.get_corner(UL)
                               + a * np.array([0.19, -0.09, 0]))

        marco.add_updater(seguir)
        marco.add_updater(pegar)
        self.add(plano, curva, punto, marco, tercios,
                 sin_aire, con_aire)
        # 1. Cámara pegada al punto: medio cuadro mira atrás
        self.play(x.animate.set_value(9), run_time=4,
                  rate_func=linear)
        # 2. El marco se adelanta un sexto de su ancho
        self.play(x.animate(rate_func=linear).set_value(12),
                  aire.animate.set_value(marco.width / 6),
                  mezcla.animate.set_value(1), run_time=2)
        # 3. Con aire: punto en el tercio izquierdo, curva delante
        self.play(x.animate.set_value(21), run_time=5,
                  rate_func=linear)
