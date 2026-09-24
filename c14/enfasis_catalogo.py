from manim import *
from congelar import congelar


class EnfasisCatalogo(Scene):
    def construct(self):
        casos = [
            ("Indicate", 0.5, lambda m: Indicate(m)),
            ("Circumscribe", 0.6, lambda m: Circumscribe(m)),
            ("Flash", 0.4, lambda m: Flash(m, flash_radius=0.7)),
            ("FocusOn", 0.7, lambda m: FocusOn(m)),
            ("Wiggle", 0.12,
             lambda m: Wiggle(m, scale_value=1.3,
                              rotation_angle=0.05 * TAU)),
            ("ShowPassingFlash", 0.5,
             lambda m: ShowPassingFlash(
                 Underline(m, color=YELLOW, stroke_width=8),
                 time_width=0.5)),
            ("ApplyWave", 0.5,
             lambda m: ApplyWave(m, amplitude=0.4)),
            ("Blink", 0.7, lambda m: Blink(m)),
        ]
        for k, (nombre, alfa, crear) in enumerate(casos):
            fila, columna = divmod(k, 4)
            centro = np.array([-5.4 + 3.6 * columna,
                               1.7 - 3.6 * fila, 0])
            formula = MathTex(r"a^2+b^2", font_size=56)
            formula.move_to(centro)
            self.add(formula)
            congelar(self, crear(formula), alfa)
            rotulo = Text(f"{nombre}  (α={alfa})",
                          font="Monospace", font_size=18)
            rotulo.move_to(centro + 1.3 * DOWN)
            self.add(rotulo)
