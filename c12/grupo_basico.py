from manim import *


class GrupoBasico(Scene):
    def construct(self):
        # Un VGroup se crea con objetos sueltos o con un iterable
        fila = VGroup(*[Square(side_length=1) for _ in range(5)])
        fila.arrange(RIGHT, buff=0.3)
        fila += Circle(radius=0.5)           # += añade al final
        fila.arrange(RIGHT, buff=0.3)
        self.play(Create(fila))
        # Indexar y rebanar, como una lista
        fila[0].set_fill(BLUE, opacity=0.8)
        fila[-1].set_color(RED)
        fila[1:4].set_fill(GREEN, opacity=0.5)
        # Recorrer con for: bajo cada figura, su índice
        rotulos = VGroup()
        for i, figura in enumerate(fila):
            rotulos.add(Integer(i).next_to(figura, DOWN))
        self.play(FadeIn(rotulos))
        # Una sola orden mueve (y escala) a todo el grupo
        todo = VGroup(fila, rotulos)
        self.play(todo.animate.scale(0.8).to_edge(UP))
        self.wait()
