from manim import *


def hanoi(n, origen, destino, auxiliar):
    """Genera los movimientos (disco, de, a) para n discos."""
    if n == 0:
        return
    yield from hanoi(n - 1, origen, auxiliar, destino)
    yield n, origen, destino
    yield from hanoi(n - 1, auxiliar, destino, origen)


class TorresHanoi(Scene):
    def construct(self):
        n, alto, base = 3, 0.45, -2.5
        x = {"A": -4, "B": 0, "C": 4}
        suelo = Line([-6, base, 0], [6, base, 0], stroke_width=6)
        postes = VGroup(*[Line([x[p], base, 0], [x[p], 0.6, 0],
                               stroke_width=8, color=GREY_B)
                          for p in x])
        nombres = VGroup(*[Text(p, font_size=32).next_to(
            [x[p], base, 0], DOWN) for p in x])
        colores = [RED_C, GOLD_C, TEAL_C, BLUE_C]
        discos = {k: RoundedRectangle(
                      corner_radius=0.15, height=alto,
                      width=1 + 0.8 * k, fill_color=colores[k - 1],
                      fill_opacity=1, stroke_width=0)
                  for k in range(1, n + 1)}
        torres = {"A": list(range(n, 0, -1)), "B": [], "C": []}
        for i, k in enumerate(torres["A"]):
            discos[k].move_to([x["A"], base + alto * (i + 0.5), 0])
        cuenta = Integer(0, font_size=40)
        rotulo = VGroup(Text("movimientos:", font_size=32), cuenta)
        rotulo.arrange(RIGHT).to_edge(UP)
        self.add(suelo, postes, nombres, *discos.values(), rotulo)

        arriba = 1.3                           # altura de vuelo
        movimientos = hanoi(n, "A", "C", "B")
        for paso, (k, de, a) in enumerate(movimientos, 1):
            torres[de].pop()
            y_final = base + alto * (len(torres[a]) + 0.5)
            torres[a].append(k)
            disco = discos[k]
            # Destinos absolutos: cada .animate se calcula
            # en el momento de crearse, no al reproducirse
            self.play(Succession(
                disco.animate.move_to([x[de], arriba, 0]),
                disco.animate.move_to([x[a], arriba, 0]),
                disco.animate.move_to([x[a], y_final, 0]),
            ), cuenta.animate.set_value(paso), run_time=1.2)
        self.wait()
