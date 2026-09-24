from manim import *


def hanoi(n, origen, destino, auxiliar):
    if n == 0:
        return
    yield from hanoi(n - 1, origen, auxiliar, destino)
    yield n, origen, destino
    yield from hanoi(n - 1, auxiliar, destino, origen)


class HanoiCuatro(Scene):
    def construct(self):
        n, alto, base = 4, 0.4, -2.5
        x = {"A": -4, "B": 0, "C": 4}
        self.add(Line([-6.5, base, 0], [6.5, base, 0]),
                 *[Line([x[p], base, 0], [x[p], 0.4, 0],
                        color=GREY_B, stroke_width=8) for p in x])
        colores = [RED_C, GOLD_C, TEAL_C, BLUE_C]
        discos = {k: RoundedRectangle(
                      corner_radius=0.12, height=alto,
                      width=0.8 + 0.7 * k, stroke_width=0,
                      fill_color=colores[k - 1], fill_opacity=1)
                  for k in range(1, n + 1)}
        torres = {"A": list(range(n, 0, -1)), "B": [], "C": []}
        for i, k in enumerate(torres["A"]):
            discos[k].move_to([x["A"], base + alto * (i + 0.5), 0])
        cuenta = Integer(0)
        total = Tex(rf"de $2^{n}-1 = {2 ** n - 1}$ movimientos")
        marcador = VGroup(cuenta, total).arrange(RIGHT).to_edge(UP)
        self.add(*discos.values(), marcador)
        movimientos = hanoi(n, "A", "C", "B")
        for paso, (k, de, a) in enumerate(movimientos, 1):
            torres[de].pop()
            y = base + alto * (len(torres[a]) + 0.5)
            torres[a].append(k)
            self.play(Succession(
                discos[k].animate.move_to([x[de], 1.2, 0]),
                discos[k].animate.move_to([x[a], 1.2, 0]),
                discos[k].animate.move_to([x[a], y, 0])),
                cuenta.animate.set_value(paso), run_time=0.6)
        self.wait()
