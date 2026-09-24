from manim import *


class Limite(Scene):
    def construct(self):
        f = MathTex(r"f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}",
                    font_size=80).shift(UP)
        f.set_color(GRAY_D)
        self.add(f, index_labels(f[0], label_height=0.22))
        # Tras leer los números: numerador 12..22, denominador 24
        g = f.copy().set_color(WHITE).shift(2.5 * DOWN)
        g[0][12:23].set_color(BLUE)
        g[0][24].set_color(RED)
        self.add(g)
