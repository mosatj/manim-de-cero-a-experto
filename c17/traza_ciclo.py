from manim import *


class Espia(Animation):
    """Desplaza su mobject y apunta cada método que Manim llama."""

    def __init__(self, mobject, desplazamiento=RIGHT * 3, **kwargs):
        super().__init__(mobject, **kwargs)
        self.desplazamiento = desplazamiento
        self.registro = [(0, "__init__()")]
        self.nivel = 0               # 1 = llamada desde dentro

    def begin(self):
        self.registro.append((0, "begin()"))
        self.nivel = 1
        super().begin()             # copia inicial + interpolate(0)
        self.nivel = 0

    def interpolate_mobject(self, alpha):
        texto = f"interpolate_mobject({alpha:.2f})"
        self.registro.append((self.nivel, texto))
        t = self.rate_func(alpha)
        # Siempre desde la copia inicial: depende solo de alpha
        self.mobject.become(self.starting_mobject)
        self.mobject.shift(t * self.desplazamiento)

    def finish(self):
        self.registro.append((0, "finish()"))
        self.nivel = 1
        super().finish()             # interpolate(1) + updaters
        self.nivel = 0

    def clean_up_from_scene(self, scene):
        self.registro.append((0, "clean_up_from_scene(scene)"))
        super().clean_up_from_scene(scene)


class TrazaCiclo(Scene):
    def construct(self):
        cuadrado = Square(0.8, color=BLUE, fill_opacity=0.6)
        cuadrado.move_to(LEFT * 4 + UP * 2.8)
        sombra = DashedVMobject(cuadrado.copy().set_fill(opacity=0))
        self.add(sombra, cuadrado)
        # 5 fotogramas a 30 fps: run_time = 5/30 s
        anim = Espia(cuadrado, run_time=5 / config.frame_rate)
        # Lo que hace Scene.play(anim), escrito a mano:
        anim._setup_scene(self)
        anim.begin()
        paso = 1 / config.frame_rate
        for t in np.arange(0, anim.run_time - 1e-9, paso):
            anim.interpolate(t / anim.run_time)
        anim.finish()
        anim.clean_up_from_scene(self)

        flecha = Arrow(sombra.get_right(), cuadrado.get_left(),
                       color=GRAY_B)
        filas = VGroup()
        for k, (nivel, texto) in enumerate(anim.registro, start=1):
            num = Text(str(k), font_size=20, color=GRAY_B)
            llamada = Text(texto, font="Menlo", font_size=22)
            if "interpolate" in texto:
                llamada.set_color(YELLOW)
            filas.add(VGroup(num, llamada))
        filas.arrange(DOWN, aligned_edge=LEFT, buff=0.13)
        filas.to_edge(LEFT, buff=1.2).to_edge(DOWN, buff=0.35)
        # Números alineados a la derecha; sangría según el nivel
        for fila, (nivel, _) in zip(filas, anim.registro):
            fila[0].align_to(filas[-1][0], RIGHT)
            fila[1].next_to(fila[0], RIGHT, buff=0.35 + 0.7 * nivel)
        self.add(flecha, filas)
