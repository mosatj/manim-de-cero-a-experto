from manim import *


def caja(texto):
    """Vértice rectangular con texto (sirve cualquier mobject)."""
    rotulo = Text(texto, font_size=22)
    marco = RoundedRectangle(corner_radius=0.12, height=0.6,
                             width=rotulo.width + 0.4,
                             fill_color=BLUE_E, fill_opacity=1,
                             stroke_color=BLUE_B)
    return VGroup(marco, rotulo)


class DigrafoCursos(Scene):
    def construct(self):
        semestres = [["Programación", "Cálculo I"],
                     ["Álgebra lineal", "Cálculo II"],
                     ["EDO", "Cálculo III"],
                     ["Métodos numéricos"]]
        cursos = [c for s in semestres for c in s]
        requisitos = [("Cálculo I", "Cálculo II"),
                      ("Cálculo II", "Cálculo III"),
                      ("Cálculo II", "EDO"),
                      ("Álgebra lineal", "EDO"),
                      ("Programación", "Métodos numéricos"),
                      ("EDO", "Métodos numéricos")]
        # Posiciones a mano: columna = semestre, de arriba abajo
        posiciones = {}
        for k, semestre in enumerate(semestres):
            for j, curso in enumerate(semestre):
                y = 1.2 * (len(semestre) - 1) - 2.4 * j
                posiciones[curso] = [-5 + 10 / 3 * k, y, 0]
        g = DiGraph(cursos, requisitos,
                    vertex_mobjects={c: caja(c) for c in cursos},
                    layout=posiciones,
                    edge_config={"stroke_width": 3,
                                 "tip_config": {"tip_length": 0.2,
                                                "tip_width": 0.2}})
        numeros = VGroup(*[
            Text(f"Semestre {k + 1}", font_size=24, color=GREY_B)
            .set_x(g[s[0]].get_x()).set_y(2.8)
            for k, s in enumerate(semestres)])
        self.play(LaggedStart(*[FadeIn(g[c]) for c in cursos]),
                  FadeIn(numeros))
        flechas = [Create(g.edges[e]) for e in requisitos]
        self.play(LaggedStart(*flechas, lag_ratio=0.3))
        self.add(g)     # desde aquí el grafo es un solo objeto
        self.wait()
