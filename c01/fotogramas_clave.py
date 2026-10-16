from manim import *


def altura(x):
    return 2.4 - 0.075 * x**2  # el arco que recorre la pelota


class FotogramasClave(Scene):
    def construct(self):
        n = 13  # fotogramas del movimiento: 3 claves y 10 intermedios
        claves = {0, n // 2, n - 1}
        tiempos = [k / (n - 1) for k in range(n)]
        # Entrada y salida lentas: los primeros y los últimos fotogramas
        # se apiñan; los del centro se separan (la pelota va más rápido)
        xs = [-5.6 + 11.2 * smooth(t) for t in tiempos]
        pelotas = VGroup()
        for k, x in enumerate(xs):
            pelota = Circle(radius=0.32).move_to([x, altura(x), 0])
            if k in claves:
                pelota.set_style(fill_color=BLUE, fill_opacity=1,
                                 stroke_color=BLUE, stroke_width=3)
            else:  # papel cebolla: los intermedios, tenues
                pelota.set_style(fill_opacity=0, stroke_color=GREY_B,
                                 stroke_width=2.5)
            pelotas.add(pelota)
        # Se numeran solo las claves: los intermedios se apiñan
        numeros = VGroup(*[
            Text(f"clave {k + 1}", font_size=26, color=BLUE)
            .next_to(pelotas[k], UP if k == n // 2 else DOWN, buff=0.15)
            for k in sorted(claves)])
        trayecto = FunctionGraph(altura, x_range=[-5.6, 5.6],
                                 color=GREY_D, stroke_width=2)
        self.add(trayecto, pelotas, numeros)

        # Cartas de espaciado: dónde cae cada fotograma en el trayecto
        def carta(posiciones, y, nombre):
            linea = Line([-5.6, y, 0], [5.6, y, 0], color=GREY_C)
            marcas = VGroup(*[
                Line([x, y - 0.22, 0], [x, y + 0.22, 0],
                     color=BLUE if k in claves else GREY_B,
                     stroke_width=5 if k in claves else 3)
                for k, x in enumerate(posiciones)])
            rotulo = Text(nombre, font_size=26).next_to(linea, LEFT)
            return VGroup(linea, marcas, rotulo)

        lineal = [-5.6 + 11.2 * t for t in tiempos]
        cartas = VGroup(carta(lineal, -1.6, "lineal"),
                        carta(xs, -2.7, "suave"))
        cartas.shift(RIGHT * 0.5)
        leyenda = Text("Cartas de espaciado (13 fotogramas)",
                       font_size=26, color=GREY_B)
        leyenda.next_to(cartas, DOWN, buff=0.35)
        self.add(cartas, leyenda)
