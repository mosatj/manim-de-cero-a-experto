from manim import *


class ZoomFormula(MovingCameraScene):
    def construct(self):
        marco = self.camera.frame
        formula = MathTex(r"f'(x)", r"=", r"\lim_{h\to 0}",
                          r"\frac{f(x+h)-f(x)}{h}", font_size=72)
        nota = Text("h se acerca a 0, pero nunca vale 0",
                    color=YELLOW).scale(0.22)
        nota.next_to(formula[2], DOWN, buff=0.15)
        numerador = formula[3][0:11]      # f(x+h)-f(x)
        self.add(formula, nota)
        marco.save_state()

        # 1) Zoom automático al numerador, con margen
        self.play(self.camera.auto_zoom([numerador], margin=1.2))
        caja = SurroundingRectangle(numerador, buff=0.08)
        rotulo = Text("cambio en f", color=BLUE).scale(0.33)
        rotulo.next_to(caja, UP, buff=0.1)
        self.play(Create(caja), FadeIn(rotulo, shift=0.2 * DOWN))
        # 2) Paneo y zoom a la nota diminuta
        detalle = [formula[2], nota]
        self.play(self.camera.auto_zoom(detalle, margin=0.4),
                  run_time=2)
        self.wait(0.5)
        # 3) Volver al plano general: todo cobra sentido
        self.play(Restore(marco), run_time=2)
