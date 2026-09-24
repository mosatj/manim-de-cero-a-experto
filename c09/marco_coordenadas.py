from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class MarcoCoordenadas(Scene):
    def construct(self):
        tenue = {"stroke_opacity": 0.35}
        self.add(NumberPlane(background_line_style=tenue))
        # Semiancho y semialto del marco (en unidades de Manim)
        ax = config.frame_width / 2    # 7.11...
        ay = config.frame_height / 2   # 4.0
        for esquina in [UL, UR, DL, DR]:
            x, y = esquina[0] * ax, esquina[1] * ay
            rotulo = MathTex(rf"({x:.2f},\ {y:.0f})", font_size=40)
            rotulo.to_corner(esquina, buff=0.2)
            self.add(BackgroundRectangle(rotulo), rotulo)
        origen = Dot(ORIGIN, radius=0.1, color=YELLOW)
        rot_origen = MathTex(r"\mathrm{ORIGIN}=(0,\ 0)")
        rot_origen.next_to(origen, UR, buff=0.1)
        # Flechas que miden el ancho y el alto
        ancho = DoubleArrow(ax * LEFT, ax * RIGHT, buff=0)
        ancho.set_color(BLUE).shift(2.6 * DOWN)
        alto = DoubleArrow(ay * DOWN, ay * UP, buff=0)
        alto.set_color(GREEN).shift(4.5 * LEFT)
        t_ancho = Text("frame_width ≈ 14.22", font_size=30)
        t_ancho.set_color(BLUE).next_to(ancho, UP, buff=0.1)
        t_ancho.shift(2 * RIGHT)
        t_alto = Text("frame_height = 8", font_size=30)
        t_alto.set_color(GREEN).rotate(PI / 2)
        t_alto.next_to(alto, RIGHT, buff=0.1).shift(1.8 * DOWN)
        for t in (rot_origen, t_ancho, t_alto):
            self.add(BackgroundRectangle(t, buff=0.06))
        self.add(ancho, alto, origen, rot_origen, t_ancho, t_alto)
