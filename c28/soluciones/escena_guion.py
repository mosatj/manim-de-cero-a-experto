from manim import *


class GuionBase(Scene):
    """Escena base: recorre un guion y llama a un método por bloque."""
    GUION = []  # lista de (bloque, segundos); la definen las subclases

    def construct(self):
        for bloque, segundos in self.GUION:
            self.next_section(bloque)
            inicio = self.time
            getattr(self, f"bloque_{bloque}")()  # p. ej. bloque_gancho()
            self.wait(max(0.1, segundos - (self.time - inicio)))


class Pitagoras(GuionBase):
    GUION = [("gancho", 3), ("figura", 4), ("formula", 3)]

    def bloque_gancho(self):
        self.play(Write(Text("¿Qué relación hay entre los lados?",
                             font_size=36).to_edge(UP)))

    def bloque_figura(self):
        self.triangulo = Polygon([-2, -1, 0], [2, -1, 0], [-2, 1.5, 0])
        self.play(Create(self.triangulo))

    def bloque_formula(self):
        formula = MathTex("a^2+b^2=c^2", font_size=64)
        self.play(Write(formula.next_to(self.triangulo, RIGHT)))
