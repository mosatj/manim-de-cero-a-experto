from manim import *


class CamaraBase(MovingCameraScene):
    """Escena madre con dos «planos» reutilizables."""

    def setup(self):
        super().setup()
        self.camera.frame.save_state()

    def enfocar(self, *mobjects, margen=1.0):
        # Devuelve la animación: quien llama decide cuándo usarla
        return self.camera.auto_zoom(list(mobjects), margin=margen)

    def plano_general(self):
        return Restore(self.camera.frame)


class TrianguloEnPlanos(CamaraBase):
    def construct(self):
        A, B, C = [-3, -2, 0], [3, -2, 0], [-3, 2, 0]
        triangulo = Polygon(A, B, C, color=BLUE)
        recto = RightAngle(Line(A, B), Line(A, C), length=0.4,
                           color=YELLOW)
        self.add(triangulo, recto)
        self.play(self.enfocar(recto, margen=1.5))
        self.play(Indicate(recto))
        self.play(self.plano_general())
        self.play(self.enfocar(triangulo, margen=0.5))
