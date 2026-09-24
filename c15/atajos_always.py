from manim import *


class AtajosAlways(Scene):
    def construct(self):
        caja = Square(1.5, color=BLUE).to_edge(LEFT)
        nombre = Text("caja", font_size=32)
        llave = Brace(caja, DOWN)
        # .always: cada método llamado se vuelve un actualizador
        nombre.always.next_to(caja, UP)
        # always(): lo mismo, en forma de función
        always(llave.match_x, caja)
        self.add(caja, nombre, llave)
        self.play(caja.animate.shift(RIGHT * 7))
