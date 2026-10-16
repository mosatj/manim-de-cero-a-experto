from manim import *

# Carta de espaciado: dónde cae cada intermedio entre dos claves
RITMOS = [linear, smooth, rate_functions.ease_in_back,
          rate_functions.ease_out_back,
          rate_functions.ease_in_out_back]


class CartaEspaciado(Scene):
    def construct(self):
        inicio, fin = -1.2, 5.6      # posiciones de las dos claves
        n = 12                       # 12 tramos: 11 intermedios
        for fila, ritmo in enumerate(RITMOS):
            y = 2.9 - 1.45 * fila
            carril = Line([inicio, y, 0], [fin, y, 0],
                          color=GRAY_C, stroke_width=2)
            nombre = Text(ritmo.__name__, font="Monospace",
                          font_size=28).next_to(carril, LEFT, 1.1)
            self.add(carril, nombre)
            for k in range(1, n):
                avance = ritmo(k / n)
                x = inicio + (fin - inicio) * avance
                medio = k == n // 2      # t = 0,5
                alto = 0.7 if medio else 0.4
                color = BLUE if medio else GRAY_B
                if avance < 0 or avance > 1:  # fuera de las claves
                    color = RED
                marca = Line(UP * alto / 2, DOWN * alto / 2,
                             color=color, stroke_width=4)
                self.add(marca.move_to([x, y, 0]))
            # Las claves se rodean con un círculo, como en la carta
            for x, numero in [(inicio, "1"), (fin, str(n + 1))]:
                clave = VGroup(Circle(0.3, color=WHITE),
                               Text(numero, font_size=28))
                self.add(clave.move_to([x, y + 0.6, 0]))
