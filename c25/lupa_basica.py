from manim import *


class LupaBasica(ZoomedScene):
    def __init__(self, **kwargs):
        # La lupa se configura al construir la escena
        super().__init__(zoom_factor=0.2, zoomed_display_width=5,
                         zoomed_display_height=3, **kwargs)

    def construct(self):
        regla = NumberLine(
            x_range=[0, 1, 0.1], length=12, include_numbers=True,
            decimal_number_config={"num_decimal_places": 1})
        regla.shift(DOWN)
        # Centésimas entre 0,3 y 0,4 (rótulo: la última cifra)
        for k in range(30, 41):
            p = regla.n2p(k / 100)
            marca = Line(p + 0.06 * UP, p + 0.06 * DOWN,
                         stroke_width=1)
            cifra = MathTex(str(k % 10), font_size=10)
            self.add(marca, cifra.next_to(p, UP, buff=0.08))
        self.add(regla)

        lente = self.zoomed_camera.frame     # lo que la lupa mira
        lente.move_to(regla.n2p(0.32) + 0.1 * UP).set_color(YELLOW)
        self.zoomed_display.display_frame.set_color(YELLOW)
        self.activate_zooming(animate=True)  # 2 animaciones
        self.play(lente.animate.move_to(regla.n2p(0.37) + 0.1 * UP),
                  run_time=2)
