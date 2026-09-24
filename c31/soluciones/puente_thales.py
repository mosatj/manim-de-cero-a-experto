from manim import *


class PuenteThales(Scene):
    """El ángulo en C vale 90° en toda la semicircunferencia."""

    def construct(self):
        A, B = LEFT * 3 + UP * 1.2, RIGHT * 3 + UP * 1.2
        centro, radio = (A + B) / 2, 3
        semicirculo = DashedVMobject(
            Arc(radio, PI, PI, arc_center=centro),
            num_dashes=40,
            color=GREY,
        )
        angulo = ValueTracker(-0.85 * PI)

        def pos_c():
            a = angulo.get_value()
            return centro + radio * np.array(
                [np.cos(a), np.sin(a), 0]
            )

        lados = always_redraw(
            lambda: VGroup(
                Line(A, pos_c(), color=GREEN),
                Line(pos_c(), B, color=GREEN),
            )
        )
        marca = always_redraw(
            lambda: Angle(
                Line(pos_c(), B),
                Line(pos_c(), A),
                radius=0.4,
                color=YELLOW,
            )
        )
        valor = always_redraw(
            lambda: DecimalNumber(
                marca.get_value(degrees=True),
                num_decimal_places=1,
                unit=r"^\circ",
                color=YELLOW,
            ).to_edge(DOWN)
        )
        self.add(semicirculo, Dot(A), Dot(B), lados, marca, valor)
        self.play(angulo.animate.set_value(-0.15 * PI), run_time=4)
