from manim import *


class PitagorasReordenamiento(Scene):
    def construct(self):
        a, b = 1.8, 3.2               # catetos; lado del cuadro a+b
        s = a + b
        O = np.array([-s / 2, -s / 2, 0])    # esquina inferior izq.
        P = lambda x, y: O + np.array([x, y, 0])
        marco = Square(s, color=WHITE).move_to(ORIGIN)
        # Cuatro copias del triángulo de catetos a, b (reparto 1)
        t1 = [Polygon(P(0, 0), P(b, 0), P(0, a)),
              Polygon(P(b, 0), P(s, 0), P(s, b)),
              Polygon(P(s, b), P(s, s), P(a, s)),
              Polygon(P(a, s), P(0, s), P(0, a))]
        # Reparto 2: dos rectángulos a x b en esquinas opuestas
        t2 = [Polygon(P(0, 0), P(b, 0), P(0, a)),
              Polygon(P(b, a), P(0, a), P(b, 0)),
              Polygon(P(b, a), P(s, a), P(b, s)),
              Polygon(P(s, s), P(b, s), P(s, a))]
        estilo = dict(fill_color=BLUE, fill_opacity=0.7,
                      stroke_color=WHITE, stroke_width=2)
        piezas = VGroup(*t1).set_style(**estilo)
        destino = VGroup(*t2).set_style(**estilo)
        hueco_c = Polygon(P(b, 0), P(s, b), P(a, s), P(0, a),
                          color=YELLOW, fill_opacity=0.35)
        rot_c = MathTex("c^2", font_size=56).move_to(hueco_c)
        self.add(marco)
        self.play(FadeIn(piezas, lag_ratio=0.3))
        self.play(FadeIn(hueco_c), Write(rot_c))
        # Mover las piezas: el área libre no cambia
        self.play(FadeOut(hueco_c), FadeOut(rot_c),
                  Transform(piezas, destino), run_time=2)
        cuad_a = Square(a, color=RED, fill_opacity=0.35)
        cuad_a.move_to(P(b + a / 2, a / 2))       # abajo a la dcha.
        cuad_b = Square(b, color=GREEN, fill_opacity=0.35)
        cuad_b.move_to(P(b / 2, a + b / 2))       # arriba a la izq.
        self.play(FadeIn(cuad_a), FadeIn(cuad_b),
                  Write(MathTex("a^2").move_to(cuad_a)),
                  Write(MathTex("b^2").move_to(cuad_b)))
        self.add(MathTex("a^2 + b^2 = c^2", font_size=56)
                 .to_edge(RIGHT, buff=0.6))
