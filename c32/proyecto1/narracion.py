from textwrap import fill
from manim import *
from manim.animation.animation import prepare_animation
from estilo import FONDO, TEXTO, TAM_SUBTITULO
from guion import texto, duracion


class GuionScene(Scene):
    """Escena base: cada frase del guion dura lo que tarda en
    decirse y aparece como subtítulo (accesibilidad y guía para
    grabar la voz después)."""

    def setup(self):
        self.camera.background_color = FONDO
        self.subtitulo = VMobject()

    def decir(self, clave, *animaciones):
        # Subtítulo en líneas de 55 caracteres como máximo
        nuevo = Text(
            fill(texto(clave), 55),
            font_size=TAM_SUBTITULO,
            color=TEXTO,
            line_spacing=0.8,
        )
        nuevo.to_edge(DOWN, buff=0.3)
        # El cambio de subtítulo va en el mismo play (0,3 s): así
        # nunca queda un subtítulo adelantado a la imagen
        cambio = [
            FadeOut(self.subtitulo, run_time=0.3),
            FadeIn(nuevo, run_time=0.3),
        ]
        # prepare_animation convierte los «.animate» en Animation
        animaciones = [
            prepare_animation(a).set_run_time(duracion(clave))
            for a in animaciones
        ]
        self.play(*cambio, *animaciones)
        if not animaciones:
            self.wait(duracion(clave) - 0.3)
        self.subtitulo = nuevo

    def construct(self):
        # Carta de prueba: renderiza el módulo para ver el estilo
        self.decir("pregunta", Write(Text("Prueba de subtítulos")))
