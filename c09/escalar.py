from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class Escalar(Scene):
    def construct(self):
        casos = [
            ("scale(1.8)", {}),
            ("about_edge=DL", {"about_edge": DL}),
            ("about_point=ORIGIN", {"about_point": ORIGIN}),
        ]
        paneles = VGroup()
        for titulo, opciones in casos:
            ejes = VGroup(Line(1.2 * LEFT, 3 * RIGHT),
                          Line(1.2 * DOWN, 3 * UP)).set_color(GRAY)
            original = Square(1, color=BLUE).move_to([1, 1, 0])
            copia = original.copy().set_color(YELLOW)
            copia.scale(1.8, **opciones)
            # El punto fijo de cada caso, para marcarlo en rojo
            fijo = original.get_center()
            if "about_edge" in opciones:
                fijo = original.get_corner(DL)
            if "about_point" in opciones:
                fijo = ORIGIN
            panel = VGroup(ejes, original, copia,
                           Dot(fijo, color=RED, radius=0.1))
            panel.add(Text(titulo, font_size=30)
                      .next_to(ejes, UP))
            paneles.add(panel)
        paneles.arrange(RIGHT, buff=0.8)
        # Que el conjunto quepa en el ancho del marco
        paneles.scale_to_fit_width(config.frame_width - 1)
        self.add(paneles.shift(0.3 * UP))
        self.add(Text("El punto rojo es el que no se mueve",
                      font_size=30, color=RED).to_edge(DOWN))
