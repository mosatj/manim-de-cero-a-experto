from manim import *


class Coreografia(Scene):
    def construct(self):
        titulo = Text("Ciclo de vida de una animación",
                      font_size=40)
        titulo.to_edge(UP)
        pasos = ["__init__", "begin", "interpolate(α)", "finish"]
        cajas = VGroup(*[
            VGroup(RoundedRectangle(width=2.9, height=1.1,
                                    corner_radius=0.2, color=BLUE),
                   Text(p, font="Monospace", font_size=24))
            for p in pasos
        ]).arrange(RIGHT, buff=0.55)
        flechas = VGroup(*[
            Arrow(a.get_right(), b.get_left(), buff=0.05)
            for a, b in zip(cajas[:-1], cajas[1:])
        ])
        base = cajas[2].get_bottom()
        bucle = CurvedArrow(base + 0.9 * RIGHT, base + 0.9 * LEFT,
                            angle=-PI, color=YELLOW)
        nota = Text("una vez por fotograma", font_size=26,
                    color=YELLOW).next_to(bucle, DOWN)

        self.play(Write(titulo))
        # Las cajas entran escalonadas, subiendo un poco
        self.play(LaggedStartMap(FadeIn, cajas, shift=0.5 * UP,
                                 lag_ratio=0.25))
        # Las flechas, estrictamente una tras otra
        self.play(Succession(*[GrowArrow(f) for f in flechas],
                             run_time=1.5))
        # El bucle y su nota, a la vez
        self.play(AnimationGroup(Create(bucle), FadeIn(nota)))
