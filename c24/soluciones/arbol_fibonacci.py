from manim import *


class ArbolFibonacci(Scene):
    def construct(self):
        vertices, aristas, rotulos = [], [], {}

        # árbol de llamadas de fib(n)
        def expandir(n, nombre):
            vertices.append(nombre)
            rotulos[nombre] = MathTex(rf"F_{{{n}}}", font_size=30,
                                      color=BLACK)
            if n >= 2:
                for m, lado in ((n - 2, "d"), (n - 1, "i")):
                    hijo = nombre + lado
                    aristas.append((nombre, hijo))
                    expandir(m, hijo)

        expandir(5, "r")
        g = Graph(vertices, aristas, labels=rotulos, layout="tree",
                  root_vertex="r", layout_scale=(6, 3),
                  vertex_config={"radius": 0.3,
                                 "fill_color": TEAL_B})
        nota = Tex(f"fib(5) hace {len(vertices)} llamadas",
                   font_size=36).to_corner(UR)
        self.play(Create(g), run_time=3)
        self.play(Write(nota))
        self.wait()
