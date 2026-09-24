from manim import *


class LayoutsGrafo(Scene):
    def construct(self):
        vertices = list(range(1, 9))
        aristas = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 5), (2, 6),
                   (3, 7), (4, 8), (5, 6), (6, 7), (7, 8), (8, 5)]
        g = Graph(vertices, aristas, labels=True, layout="circular",
                  layout_scale=2.8, vertex_config={"radius": 0.28})
        nombre = Text('layout="circular"', font_size=32)
        self.play(Create(g), Write(nombre.to_edge(UP)))
        opciones = [
            ("shell", {"nlist": [[1, 2, 3, 4], [5, 6, 7, 8]]}),
            ("kamada_kawai", {}),
            ("spring", {"seed": 3}),     # semilla: siempre igual
        ]
        for layout, config in opciones:
            nuevo = Text(f'layout="{layout}"', font_size=32)
            self.play(
                g.animate.change_layout(layout, layout_scale=2.8,
                                        layout_config=config),
                Transform(nombre, nuevo.to_edge(UP)),
                run_time=1.5,
            )
            self.wait(0.5)
