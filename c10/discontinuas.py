from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class Discontinuas(Scene):
    def construct(self):
        casos = [
            ("num_dashes=15", {}),
            ("num_dashes=40", {"num_dashes": 40}),
            ("dashed_ratio=0.2", {"dashed_ratio": 0.2}),
            ("dashed_ratio=0.8", {"dashed_ratio": 0.8}),
        ]
        fila = VGroup()
        for t, opciones in casos:
            base = Star(outer_radius=1.2, color=YELLOW)
            rayada = DashedVMobject(base, **opciones)
            fila.add(VGroup(rayada, Text(t, font_size=24)
                            .next_to(rayada, DOWN)))
        fila.arrange(RIGHT, buff=0.5)
        self.add(fila)
