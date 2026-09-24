from manim import *


class MigrarGL(MovingCameraScene):     # self.frame -> camera.frame
    def construct(self):
        titulo = Tex("Área del círculo")             # TexText
        formula = MathTex(r"A=\pi r^2")             # Tex en ManimGL
        VGroup(titulo, formula).arrange(DOWN)
        circulo = Circle(1, color=BLUE).next_to(formula, DOWN)
        self.play(Create(circulo))                   # ShowCreation
        self.play(Write(titulo), FadeIn(formula, shift=UP))
        marco = self.camera.frame
        self.play(marco.animate.scale(0.6).move_to(formula))
