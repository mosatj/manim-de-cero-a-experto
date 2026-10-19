from manim import *
from _plano_simulado import PlanoSimulado

PETROLEO, GRANATE, CREMA = "#0B2A3C", "#B04A5A", "#E9F2F7"


class RotuloInferior(Scene):
    """Rótulo para superponer: con -t, el fondo es transparente."""
    nombre = "Moisés Samuel Toledo Julián"
    cargo = "Docente de Matemática"
    permanencia = 4  # segundos de lectura
    con_salida = True

    def fondo(self):
        pass  # la grabación la pone el editor, debajo

    def crear(self):
        nombre = Text(self.nombre, font_size=44, weight=BOLD,
                      color=CREMA)
        cargo = Text(self.cargo, font_size=34, color=CREMA)
        textos = VGroup(nombre, cargo).arrange(
            DOWN, aligned_edge=LEFT, buff=0.2)
        banda = Rectangle(width=textos.width + 1.1,
                          height=textos.height + 0.7,
                          fill_color=PETROLEO, fill_opacity=0.95,
                          stroke_width=0)
        barra = Rectangle(width=0.16, height=banda.height,
                          fill_color=GRANATE, fill_opacity=1,
                          stroke_width=0)
        barra.next_to(banda, LEFT, buff=0)
        # Dentro de la zona segura de rótulos (90 % del cuadro)
        VGroup(barra, banda).align_to(0.9 * config.left_side, LEFT)
        VGroup(barra, banda).align_to(0.8 * config.bottom, DOWN)
        textos.move_to(banda).align_to(banda, LEFT)
        textos.shift(0.55 * RIGHT)
        return barra, banda, textos

    def construct(self):
        self.fondo()
        barra, banda, textos = self.crear()
        self.play(GrowFromEdge(barra, DOWN), run_time=0.3)
        self.play(GrowFromEdge(banda, LEFT), run_time=0.4)
        self.play(FadeIn(textos, shift=0.3 * RIGHT), run_time=0.4)
        # Sin congelar: la secuencia PNG conserva toda la espera
        self.wait(self.permanencia, frozen_frame=False)
        if self.con_salida:
            self.play(FadeOut(barra, banda, textos), run_time=0.4)


class RotuloSobreVideo(RotuloInferior):
    """Muestra para revisar el rótulo sobre una imagen de prueba"""
    permanencia = 0.5
    con_salida = False

    def fondo(self):
        self.add(PlanoSimulado())
