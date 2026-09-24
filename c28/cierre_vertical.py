from manim import *
from cierre_adaptable import componer_cierre

config.pixel_width, config.pixel_height = 1080, 1920
config.frame_width, config.frame_height = 8, 8 * 16 / 9


class CierreVertical(Scene):
    def construct(self):
        self.play(FadeIn(componer_cierre()))
