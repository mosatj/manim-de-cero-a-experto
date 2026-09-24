from manim import *


class RelojAnalogico(Scene):
    def construct(self):
        esfera = Circle(radius=2.8, color=GREY_B)
        marcas = VGroup(*[
            Line(2.5 * UP, 2.8 * UP, stroke_width=[6, 2, 2][k % 3])
            .rotate(-k * TAU / 12, about_point=ORIGIN)
            for k in range(12)])
        # Una sola fuente de verdad: los minutos transcurridos
        reloj = ValueTracker(10 * 60 + 5)            # 10:05
        reloj.add_updater(lambda m, dt: m.increment_value(30 * dt))

        def aguja(fraccion, largo):          # sentido horario
            angulo = PI / 2 - TAU * fraccion
            return largo * rotate_vector(RIGHT, angulo)

        horario = Line(ORIGIN, UP, stroke_width=10, color=BLUE)
        minutero = Line(ORIGIN, UP, stroke_width=6, color=TEAL)
        horario.add_updater(lambda m: m.put_start_and_end_on(
            ORIGIN, aguja(reloj.get_value() / 720, 1.5)))
        minutero.add_updater(lambda m: m.put_start_and_end_on(
            ORIGIN, aguja(reloj.get_value() / 60, 2.3)))

        def lectura():
            total = int(reloj.get_value()) % 720
            horas = total // 60 or 12       # las 0 h se leen «12»
            texto = f"{horas:02d}:{total % 60:02d}"
            return Text(texto, font_size=48).to_corner(UR)

        digital = always_redraw(lectura)
        # El tracker va primero: todos leen su valor ya actualizado
        self.add(reloj, esfera, marcas, horario, minutero,
                 digital, Dot(color=WHITE))
        self.wait(4)  # 4 s reales = 120 min del reloj
