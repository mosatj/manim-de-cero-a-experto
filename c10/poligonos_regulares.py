from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class PoligonosRegulares(Scene):
    def construct(self):
        colores = color_gradient([BLUE, YELLOW, RED], 8)
        fila = VGroup()
        for n, color in zip(range(3, 11), colores):
            forma = RegularPolygon(n, color=color)
            forma.set_fill(color, 0.3).scale(0.7)
            fila.add(VGroup(forma, MathTex(f"n={n}", font_size=34)
                            .next_to(forma, DOWN)))
        fila.arrange(RIGHT, buff=0.3).to_edge(UP, buff=0.6)
        # Estrellas: Star (sin trazos interiores) y RegularPolygram
        estrellas = VGroup(
            Star(5, color=YELLOW, fill_opacity=0.4),
            Star(7, density=3, color=GREEN, fill_opacity=0.4),
            Star(12, inner_radius=0.8, color=BLUE,
                 fill_opacity=0.4),
            RegularPolygram(7, density=3, color=RED),
            RegularPolygram(9, density=4, color=PURPLE),
        )
        rotulos = ["Star(5)", "Star(7, density=3)",
                   "Star(12, inner_radius=0.8)",
                   "RegularPolygram(7, density=3)",
                   "RegularPolygram(9, density=4)"]
        abajo = VGroup()
        for e, t in zip(estrellas, rotulos):
            texto = Text(t, font_size=28).next_to(e, DOWN)
            abajo.add(VGroup(e, texto))
        abajo.arrange(RIGHT, buff=0.35)
        abajo.scale_to_fit_width(config.frame_width - 1)
        abajo.to_edge(DOWN, buff=0.6)
        self.add(fila, abajo)
