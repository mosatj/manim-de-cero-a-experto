from manim import *


class VDictMarcador(Scene):
    def construct(self):
        # VDict: un grupo cuyas piezas se buscan por nombre
        marcador = VDict({
            "local": Text("Local", font_size=40),
            "goles": MathTex("0", "-", "0", font_size=96),
            "visita": Text("Visita", font_size=40),
        })
        marcador["local"].next_to(marcador["goles"], LEFT, buff=1)
        marcador["visita"].next_to(marcador["goles"], RIGHT, buff=1)
        self.add(marcador)
        # Reemplazar una pieza por su clave
        nuevo = MathTex("1", "-", "0", font_size=96, color=YELLOW)
        nuevo.move_to(marcador["goles"])
        self.play(Transform(marcador["goles"], nuevo))
        self.play(Indicate(marcador["local"]))
        self.wait()
