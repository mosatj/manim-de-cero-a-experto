from manim import *
from manim_voiceover import VoiceoverScene

from servicio_ensayo import ServicioEnsayo


class VozMarcadores(VoiceoverScene):
    def construct(self):
        self.set_speech_service(ServicioEnsayo())
        a, b, c = [-3, -1.5, 0], [3, -1.5, 0], [1, 2, 0]
        triangulo = Polygon(a, b, c, color=WHITE)
        base = Line(a, b, color=BLUE_E, stroke_width=8)
        pie = [1, -1.5, 0]
        altura = DashedLine(c, pie, color=RED_E)
        formula = MathTex(r"A=", r"b", r"\cdot", r"h", r"\,/\,2")
        formula.to_edge(UP).set_color_by_tex("b", BLUE_E)
        formula[3].set_color(RED_E)
        self.add(triangulo)

        with self.voiceover(
            text="El área es <bookmark mark='b'/>la base por "
                 "<bookmark mark='h'/>la altura, "
                 "<bookmark mark='m'/>dividido entre dos."
        ) as t:
            self.wait_until_bookmark("b")
            self.play(Create(base), FadeIn(formula[:2]),
                      run_time=0.6)
            self.wait_until_bookmark("h")
            self.play(Create(altura), FadeIn(formula[2:4]),
                      run_time=0.6)
            self.wait_until_bookmark("m")
            self.play(Write(formula[4]), run_time=0.6)

        marcas = [f"{m}: {s - t.start_t:.2f} s"
                  for m, s in t.bookmark_times.items()]
        rotulo = Text("   ".join(marcas), font_size=26)
        self.add(rotulo.to_edge(DOWN))
