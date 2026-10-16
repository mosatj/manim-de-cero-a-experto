from manim import *
from funcion import volumen_discos
from piezas import ejes2d, curva, region_2d, rectangulos
from piezas import discos_2d, rotulo_discos, rotulo_exacto
from estilo import COLOR_CURVA, TAM_TITULO


class RegionYDiscos(Scene):
    """La idea en el plano: la región gira y cada rectángulo se
    convierte en un disco. Primero se entiende aquí; la 3D viene
    después."""

    def construct(self):
        ejes = ejes2d().shift(DOWN * 0.4)
        grafica = curva(ejes)
        etiqueta = MathTex(
            r"y=f(x)", font_size=TAM_TITULO, color=COLOR_CURVA
        ).next_to(ejes.c2p(4, 1.2), UR, buff=0.1)
        titulo = Tex(
            "Volumen del sólido de revolución",
            font_size=TAM_TITULO,
        ).to_edge(UP, buff=0.3)
        self.play(Create(ejes), Write(titulo))
        self.play(Create(grafica), FadeIn(etiqueta))

        # Bloque 1: la región y su imagen al girar (el borde -f)
        region = region_2d(ejes, grafica)
        espejo = DashedVMobject(
            curva(ejes, espejo=True), num_dashes=40
        )
        self.play(FadeIn(region))
        self.play(Create(espejo), run_time=1.5)

        # Bloque 2: rectángulos que se vuelven discos (n = 4)
        rotulo = rotulo_discos(4, volumen_discos(4)).next_to(
            titulo, DOWN, buff=0.25
        )
        rects = rectangulos(ejes, grafica, 4)
        discos = discos_2d(ejes, 4)
        self.play(FadeIn(rects), Write(rotulo))
        self.play(
            FadeOut(region),
            ReplacementTransform(rects, discos),
            run_time=1.5,
        )

        # Bloque 3: más discos, mejor aproximación
        for n in (8, 16):
            nuevos = discos_2d(ejes, n)
            nuevo_rotulo = rotulo_discos(n, volumen_discos(n))
            nuevo_rotulo.move_to(rotulo)
            self.play(
                ReplacementTransform(discos, nuevos),
                Transform(rotulo, nuevo_rotulo),
                run_time=1.2,
            )
            discos = nuevos
            self.wait(0.5)

        # Cierre: el valor exacto, junto a la aproximación
        exacto = rotulo_exacto().next_to(rotulo, DOWN, buff=0.2)
        self.play(Write(exacto))
        self.wait()
