from manim import *


class LeccionScene(Scene):
    """Plantilla: numera los apartados y deja su título arriba."""

    COLOR_TITULO = "#2A8FBD"

    def setup(self):
        super().setup()
        self.numero_apartado = 0
        self.titulo_actual = VMobject()          # marcador vacío
        self.add(self.titulo_actual)

    def apartado(self, texto):
        self.numero_apartado += 1
        rotulo = f"{self.numero_apartado}. {texto}"
        nuevo = Text(rotulo, font_size=40, color=self.COLOR_TITULO)
        nuevo.to_corner(UL, buff=0.5)
        self.next_section(texto)          # una sección por apartado
        self.play(FadeTransform(self.titulo_actual, nuevo))
        self.titulo_actual = nuevo


class LeccionCirculo(LeccionScene):
    def construct(self):
        self.apartado("La circunferencia")
        c = Circle(radius=2, color=BLUE)
        self.play(Create(c))
        self.apartado("Su radio")
        radio = Line(ORIGIN, RIGHT * 2, color=YELLOW)
        self.play(Create(radio))
        self.wait()


class LeccionCuadrado(LeccionScene):
    COLOR_TITULO = "#B3174A"                     # se sobrescribe

    def construct(self):
        self.apartado("El cuadrado")
        self.play(Create(Square(3, color=RED)))
        self.wait()
