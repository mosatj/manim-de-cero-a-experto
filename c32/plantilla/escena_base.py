from textwrap import fill
from manim import *
from manim.animation.animation import prepare_animation
from estilo import FONDO, TEXTO, TAM_SUBTITULO
from guion import texto, duracion


class ProyectoScene(Scene):
    """Escena base del proyecto: fondo común, subtítulos y el
    método decir(), que dura lo que tarda en leerse cada frase."""

    def setup(self):
        self.camera.background_color = FONDO
        self.subtitulo = VMobject()

    def decir(self, clave, *animaciones):
        nuevo = Text(fill(texto(clave), 55), color=TEXTO,
                     font_size=TAM_SUBTITULO)
        nuevo.to_edge(DOWN, buff=0.3)
        cambio = [FadeOut(self.subtitulo, run_time=0.3),
                  FadeIn(nuevo, run_time=0.3)]
        tiempo = duracion(clave)
        animaciones = [prepare_animation(a).set_run_time(tiempo)
                       for a in animaciones]
        self.play(*cambio, *animaciones)
        if not animaciones:
            self.wait(duracion(clave) - 0.3)
        self.subtitulo = nuevo

    def construct(self):
        # Carta de ajuste: este archivo solo muestra el subtítulo
        self.decir("gancho")
