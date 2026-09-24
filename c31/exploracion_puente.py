from manim import *


class ExploracionPuente(Scene):
    def construct(self):
        # Situación semirreal: un puente de A a B sobre un lago
        lago = Ellipse(
            width=4, height=2.2, color=BLUE_D, fill_opacity=0.35
        ).shift(UP * 1.2)
        A = Dot(lago.get_center() + LEFT * 3, color=YELLOW)
        B = Dot(lago.get_center() + RIGHT * 3, color=YELLOW)
        rotulos = VGroup(
            MathTex("A").next_to(A, LEFT),
            MathTex("B").next_to(B, RIGHT),
        )
        puente = DashedLine(
            A.get_center(), B.get_center(), color=GREY
        )
        self.add(lago, puente, A, B, rotulos)

        # C recorre la orilla de abajo; el parámetro es un ángulo
        angulo = ValueTracker(-0.35 * PI)
        radio = (B.get_center() - A.get_center())[0] / 2
        centro = (A.get_center() + B.get_center()) / 2
        km = 7.97 / (2 * radio)  # escala: AB mide 7,97 km

        def pos_c():
            a = angulo.get_value()
            return centro + radio * np.array(
                [np.cos(a), np.sin(a), 0]
            )

        C = always_redraw(lambda: Dot(pos_c(), color=RED))
        lados = always_redraw(
            lambda: VGroup(
                Line(A.get_center(), pos_c(), color=GREEN),
                Line(pos_c(), B.get_center(), color=GREEN),
            )
        )

        def medida(nombre, extremo):
            valor = DecimalNumber(
                km * np.linalg.norm(pos_c() - extremo.get_center()),
                font_size=36,
                unit=r"\text{km}",
                unit_buff_per_font_unit=0.004,
            )
            return VGroup(
                MathTex(nombre + "=", font_size=36), valor
            ).arrange(RIGHT, buff=0.1)

        medidas = always_redraw(
            lambda: (
                VGroup(medida("AC", A), medida("BC", B))
                .arrange(RIGHT, buff=0.8)
                .to_edge(DOWN)
            )
        )
        self.play(Create(lados), FadeIn(C), FadeIn(medidas))
        # Última parada: los datos de la tesis (AC = 4,25 km)
        final = 2 * np.arcsin(4.25 / 7.97) - PI
        for destino in (-0.85 * PI, -0.2 * PI, final):
            self.play(angulo.animate.set_value(destino), run_time=2)

        # Con C en la semicircunferencia, el ángulo en C es recto
        recto = RightAngle(
            Line(pos_c(), A.get_center()),
            Line(pos_c(), B.get_center()),
            length=0.3,
            color=YELLOW,
        )
        pregunta = Text(
            "¿Cómo calcular AB sin cruzar el lago?", font_size=30
        ).to_edge(UP)
        self.play(Create(recto), Write(pregunta))
