from manim import *


def congelar(escena, animacion, alfa):
    """Detiene la animación en el instante alfa (0 <= alfa <= 1)
    y deja ese fotograma en la escena. Son los mismos pasos
    que da self.play() antes de dibujar cada fotograma."""
    animacion._setup_scene(escena)  # añade los «introductores»
    animacion.begin()               # guarda el estado inicial
    animacion.update_mobjects(0)    # pone al día los auxiliares
    animacion.interpolate(alfa)     # calcula el fotograma alfa
    escena.add(animacion.mobject)
    return animacion.mobject
