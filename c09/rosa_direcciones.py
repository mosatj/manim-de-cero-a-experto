from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class RosaDirecciones(Scene):
    def construct(self):
        direcciones = {
            "UP": UP, "DOWN": DOWN, "LEFT": LEFT, "RIGHT": RIGHT,
            "UL": UL, "UR": UR, "DL": DL, "DR": DR,
        }
        escala = 2.6  # alargamos los vectores para verlos
        for nombre, v in direcciones.items():
            # Las diagonales, en amarillo: no son unitarias
            color = BLUE if np.linalg.norm(v) == 1 else YELLOW
            flecha = Arrow(ORIGIN, escala * v, buff=0)
            flecha.set_color(color)
            rotulo = Text(nombre, font_size=34, color=color)
            rotulo.next_to(flecha.get_end(), v, buff=0.15)
            self.add(flecha, rotulo)
        self.add(Dot(color=WHITE), Text("ORIGIN", font_size=26)
                 .next_to(ORIGIN, DR, buff=0.12))
        nota = MathTex(r"\mathrm{UR}=\mathrm{UP}+\mathrm{RIGHT}"
                       r"=[1,1,0]", font_size=40)
        self.add(nota.to_corner(UL))
