from manim import *
from manim_voiceover import VoiceoverScene

from servicio_ensayo import ServicioEnsayo


class VozPrimera(VoiceoverScene):
    def construct(self):
        self.set_speech_service(ServicioEnsayo())
        circulo = Circle(radius=2, color=BLUE)
        radio = Line(ORIGIN, 2 * RIGHT, color=YELLOW)

        frase = "Dibujamos una circunferencia."
        with self.voiceover(text=frase) as t:
            self.play(Create(circulo), run_time=t.duration)

        with self.voiceover(text="Y su radio mide dos.") as t:
            self.play(Create(radio), run_time=t.duration / 2)
            self.play(Write(MathTex("r=2").next_to(radio, UP)))

        rotulo = Text(f"Última frase: {t.duration:.2f} s")
        self.add(rotulo.to_edge(DOWN))
