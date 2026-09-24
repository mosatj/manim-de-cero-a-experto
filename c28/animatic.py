from manim import *
from guion_impares import GUION, duracion
from storyboard_impares import vineta


def rotulo_voz(texto):
    """Banda inferior con la narración provisional (para ensayar)."""
    voz = Paragraph(*texto_en_lineas(texto, 50), font_size=30,
                    alignment="center")
    fondo = BackgroundRectangle(voz, color=BLACK, fill_opacity=0.8,
                                buff=0.2)
    return VGroup(fondo, voz).to_edge(DOWN, buff=0.3)


def texto_en_lineas(texto, max_car=60):
    lineas, actual = [], ""
    for palabra in texto.split():
        if actual and len(actual) + len(palabra) >= max_car:
            lineas.append(actual)
            actual = palabra
        else:
            actual = f"{actual} {palabra}".strip()
    return lineas + [actual]


class Animatic(Scene):
    def construct(self):
        # Viñetas fijas + voz escrita + duración real: el ritmo se
        # juzga antes de programar una sola animación
        t = 0.0
        for n, bloque in enumerate(GUION[:4], start=1):  # 4 viñetas
            imagen = vineta(n).shift(0.6 * UP)
            voz = rotulo_voz(bloque["voz"])
            reloj = Text(f"{int(t // 60)}:{round(t % 60):02d}",
                         font="Monospace", font_size=24, color=GREY_B)
            reloj.to_corner(UR)
            self.clear()
            self.add(imagen, voz, reloj)
            self.wait(duracion(bloque))
            t += duracion(bloque)
