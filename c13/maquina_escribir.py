from manim import *


class MaquinaEscribir(Scene):
    def construct(self):
        linea1 = Text("Letra a letra...", font_size=48)
        linea2 = Text("...y con cursor.", font_size=48)
        VGroup(linea1, linea2).arrange(DOWN, buff=0.8)
        cursor = Rectangle(width=0.08, height=0.6, color=YELLOW,
                           fill_opacity=1, stroke_width=0)

        self.play(AddTextLetterByLetter(linea1, time_per_char=0.08))
        self.play(TypeWithCursor(linea2, cursor, time_per_char=0.08,
                                 keep_cursor_y=False))
        self.play(Blink(cursor, blinks=2))
