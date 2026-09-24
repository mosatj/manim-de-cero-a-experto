from minimanim import *


class MiEscena(Escena):
    def construir(self):            # sobrescribimos el gancho
        circulo = Circulo(radio=2, color="rojo")
        cuadrado = Cuadrado(lado=3, color="azul")
        fila = Grupo(circulo, cuadrado).ordenar(separacion=1)
        self.reproducir(Crear(fila))
        self.esperar(0.5)
        self.reproducir(Desplazar(cuadrado, 0.5, 0.5, duracion=2))
        print("  fila[0] es", fila[0], "| len(fila) =", len(fila))


MiEscena().render()
