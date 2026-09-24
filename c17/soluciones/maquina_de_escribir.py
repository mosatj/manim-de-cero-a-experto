from manim import *


class MaquinaDeEscribir(Animation):
    """Muestra un Text letra a letra, con un cursor que parpadea."""

    def __init__(self, texto, tiempo_por_letra=0.08,
                 color_cursor=YELLOW, parpadeo=0.5, **kwargs):
        self.texto = texto
        self.letras = texto.family_members_with_points()
        alto = texto[0].height * 1.3
        self.cursor = Rectangle(width=0.06, height=alto)
        self.cursor.set_fill(color_cursor, 1).set_stroke(width=0)
        self.parpadeo = parpadeo
        kwargs.setdefault("run_time", tiempo_por_letra * len(texto))
        kwargs.setdefault("rate_func", linear)
        grupo = VGroup(texto, self.cursor)
        super().__init__(grupo, introducer=True, **kwargs)

    def interpolate_mobject(self, alpha):
        n = len(self.letras)
        visibles = int(np.ceil(self.rate_func(alpha) * n))
        for i, letra in enumerate(self.letras):
            letra.set_opacity(1 if i < visibles else 0)
        # El cursor va detrás de la última letra visible
        ultima = self.letras[max(visibles - 1, 0)]
        self.cursor.next_to(ultima, RIGHT, buff=0.06)
        self.cursor.match_y(ultima)
        # Parpadea según el tiempo transcurrido (alpha * run_time)
        segundos = alpha * self.run_time
        par = int(segundos / self.parpadeo) % 2 == 0
        encendido = visibles < n or par
        self.cursor.set_opacity(1 if encendido else 0)


class EscenaMaquina(Scene):
    def construct(self):
        codigo = Text('print("Hola, Manim")', font="Menlo",
                      font_size=40)
        codigo.to_edge(LEFT, buff=1.5).shift(UP)
        salida = Text("Hola, Manim", font="Menlo", font_size=40,
                      color=GRAY_A).next_to(codigo, DOWN, buff=0.8,
                                            aligned_edge=LEFT)
        self.play(MaquinaDeEscribir(codigo))
        # run_time explícito: escribe más despacio que el primero
        self.play(MaquinaDeEscribir(salida, color_cursor=BLUE),
                  run_time=2)
        self.wait()
