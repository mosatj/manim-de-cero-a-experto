from manim import *

PESOS = {("A", "B"): 4, ("A", "C"): 2, ("B", "C"): 1,
         ("B", "D"): 5, ("C", "D"): 8, ("C", "E"): 10,
         ("D", "E"): 2, ("D", "F"): 6, ("E", "F"): 2}
POSICIONES = {"A": [-5.5, 0, 0], "B": [-3, 2, 0], "C": [-3, -2, 0],
              "D": [0, 2, 0], "E": [0, -2, 0], "F": [2.5, 0, 0]}


class Kruskal(Scene):
    def construct(self):
        g = Graph(list(POSICIONES), list(PESOS), layout=POSICIONES,
                  labels=True, vertex_config={"radius": 0.32},
                  edge_config={"stroke_color": GREY_C})
        pesos = [MathTex(str(w), font_size=30).move_to(g.edges[e])
                 .add_background_rectangle()
                 for e, w in PESOS.items()]
        self.add(g, *pesos)
        # conjuntos disjuntos
        padre = {v: v for v in POSICIONES}

        def raiz(v):
            while padre[v] != v:
                v = padre[v]
            return v

        total = 0
        for (u, v), w in sorted(PESOS.items(), key=lambda t: t[1]):
            ru, rv = raiz(u), raiz(v)
            # no forma ciclo: entra
            if ru != rv:
                padre[ru] = rv
                total += w
                arista = g.edges[(u, v)]
                self.play(arista.animate.set_stroke(GREEN_C, 8))
            # formaría un ciclo
            else:
                arista = g.edges[(u, v)]
                self.play(arista.animate.set_stroke(opacity=0.2))
        self.play(Write(MathTex(rf"\text{{peso total}} = {total}")
                        .to_edge(DOWN)))
        self.wait()
