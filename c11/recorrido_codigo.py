from manim import *

FUENTE = '''resultado = 1
for k in range(2, 5):
    resultado *= k
print(resultado)'''


class RecorridoCodigo(Scene):
    def construct(self):
        listado = Code(code_string=FUENTE, language="python",
                       formatter_style="monokai",
                       paragraph_config={"font": "Monospace",
                                         "font_size": 30,
                                         "line_spacing": 1})
        valor = Variable(1, Text("resultado", font="Monospace",
                                 font_size=32), var_type=Integer)
        VGroup(listado, valor).arrange(RIGHT, buff=1.2)
        lineas = listado.code_lines

        def caja(n):              # marco a medida de la línea n
            return SurroundingRectangle(lineas[n], color=YELLOW,
                                        buff=0.06)

        marco = caja(0)
        self.add(listado, valor)
        self.play(Create(marco))
        for k in [2, 3, 4]:                # las vueltas del bucle
            self.play(Transform(marco, caja(1)))
            self.play(Transform(marco, caja(2)),
                      valor.tracker.animate.set_value(
                          valor.tracker.get_value() * k))
        self.play(Transform(marco, caja(3)))
        self.wait()
