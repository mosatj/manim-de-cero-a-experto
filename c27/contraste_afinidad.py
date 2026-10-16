from manim import *

f = lambda x: 0.2 * x**3 - 1.2 * x + 3
A, B, C = -1.5, 3, 1.5      # f'(C) = pendiente de la secante AB


def piezas():
    ejes = Axes(x_range=[-2.5, 3.5], y_range=[0, 5.5], x_length=7,
                y_length=5.4, tips=False).to_edge(LEFT, buff=0.6)
    curva = ejes.plot(f, x_range=[-2.4, 3.15])
    secante = Line(ejes.c2p(A, f(A)), ejes.c2p(B, f(B)))
    m = (f(B) - f(A)) / (B - A)
    tangente = ejes.plot(lambda x: f(C) + m * (x - C),
                         x_range=[C - 1.7, C + 1.7])
    extremos = VGroup(*[Dot(ejes.c2p(x, f(x))) for x in (A, B)])
    punto_c = Dot(ejes.c2p(C, f(C)))
    rotulos = VGroup(*[MathTex(t, font_size=40).next_to(
        ejes.c2p(x, 0), DOWN) for t, x in zip("abc", (A, B, C))])
    formula = MathTex(r"f'(c)", "=", r"\frac{f(b)-f(a)}{b-a}")
    titulo = Text("Teorema del valor medio", font_size=36)
    return (ejes, curva, secante, tangente, extremos, punto_c,
            rotulos, formula, titulo)


class AfinidadTotal(Scene):
    def construct(self):
        p = piezas()
        todo = VGroup(*p).set_color(WHITE)       # un solo color y tono
        for linea in p[:4]:
            linea.set_stroke(width=3)            # un solo grosor
        p[7].font_size = 40                      # fórmula = rótulos
        VGroup(p[8], p[7]).arrange(DOWN, buff=0.8).to_edge(RIGHT)
        self.play(Create(todo))


class ContrasteFoco(Scene):
    def construct(self):
        (ejes, curva, secante, tangente, extremos, punto_c,
         rotulos, formula, titulo) = piezas()
        # Tono: el contexto retrocede
        ejes.set_stroke(GRAY, 2, opacity=0.5)
        titulo.set_color(GRAY).font_size = 30
        VGroup(secante, extremos, rotulos[:2]).set_color(GRAY)
        curva.set_stroke(BLUE, 4)
        # Tamaño y color: el protagonista gana en los tres a la vez
        tangente.set_stroke(ORANGE, 9)
        punto_c.set_color(ORANGE).scale(1.8)
        rotulos[2].set_color(ORANGE).scale(1.3)
        formula.font_size = 60
        formula[0].set_color(ORANGE)
        formula[2].set_color(GRAY)               # = color de la secante
        titulo.to_corner(UR)
        formula.to_edge(RIGHT, buff=0.5)
        contexto = VGroup(ejes, curva, secante, extremos,
                          rotulos[:2], titulo)
        self.add(contexto)
        self.play(Create(tangente), GrowFromCenter(punto_c),
                  FadeIn(rotulos[2]))
        self.play(Write(formula))
