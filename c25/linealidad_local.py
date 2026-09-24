from manim import *


class LinealidadLocal(ZoomedScene):
    def __init__(self, **kwargs):
        super().__init__(
            zoom_factor=0.25,                # aumento inicial ×4
            zoomed_display_width=4, zoomed_display_height=4,
            zoomed_display_corner=UR,
            # Trazos 4 veces más finos dentro de la lupa
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
                "background_opacity": 1,
                "cairo_line_width_multiple": 0.0025},
            **kwargs)

    def construct(self):
        ejes = Axes(x_range=[-1, 3, 1], y_range=[-1, 4, 1],
                    x_length=6, y_length=6).to_edge(LEFT)
        f = lambda x: 0.5 * x**2 + 0.3
        curva = ejes.plot(f, x_range=[-1, 2.6], color=BLUE)
        a = 1.5                                   # punto de estudio
        P = Dot(ejes.c2p(a, f(a)), radius=0.02, color=YELLOW)
        tangente = ejes.plot(lambda x: f(a) + a * (x - a),
                             x_range=[0.4, 2.6], color=YELLOW,
                             stroke_width=2)
        texto = MathTex(r"y=\tfrac12x^2+0{,}3", color=BLUE)
        texto.next_to(ejes, RIGHT, buff=0.5).shift(2 * DOWN)
        self.add(ejes, curva, P, texto)

        lente = self.zoomed_camera.frame
        lente.move_to(P).set_color(YELLOW)
        self.zoomed_display.display_frame.set_color(YELLOW)
        self.activate_zooming(animate=True)
        self.play(Create(tangente))
        # Más aumento: la lente se encoge y la ventana no cambia
        self.play(lente.animate.scale(0.5), run_time=3)
        factor = 1 / self.get_zoom_factor()
        aumento = MathTex(rf"\times{factor:.0f}", color=YELLOW)
        aumento.next_to(self.zoomed_display, DOWN)
        self.play(Write(aumento))
