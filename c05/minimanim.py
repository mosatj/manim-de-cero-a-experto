"""minimanim: mini-biblioteca de figuras en Python puro (cap. 5).

Imita, a escala de juguete, la arquitectura de Manim:
Figura ~ Mobject, Grupo ~ VGroup, Animacion ~ Animation,
Escena ~ Scene. Dibuja con caracteres en la terminal.
"""
import math

# Cada color se «pinta» con un carácter distinto en la terminal
CARACTER = {"blanco": "*", "rojo": "#", "azul": "o", "verde": "+"}


class Figura:
    """Todo lo que se dibuja (el papel de Mobject)."""

    def __init__(self, color="blanco"):
        self.color = color
        self.puntos = []        # vértices (x, y) de la figura
        self.subfiguras = []    # composición: figuras contenidas
        self.visible = 1.0     # fracción del contorno que se dibuja
        self.generar_puntos()

    def generar_puntos(self):
        """Gancho: cada subclase lo sobrescribe con su geometría."""

    def familia(self):
        """La figura y todas sus subfiguras, recursivamente."""
        todas = [self]
        for sub in self.subfiguras:
            todas.extend(sub.familia())
        return todas

    def limites(self):
        pts = [p for f in self.familia() for p in f.puntos]
        xs = [x for x, _ in pts]
        ys = [y for _, y in pts]
        return min(xs), max(xs), min(ys), max(ys)

    def centro(self):
        x0, x1, y0, y1 = self.limites()
        return (x0 + x1) / 2, (y0 + y1) / 2

    def aplicar(self, funcion):
        """Aplica funcion(x, y) -> (x', y') a toda la familia."""
        for f in self.familia():
            f.puntos = [funcion(x, y) for x, y in f.puntos]
        return self

    def desplazar(self, dx, dy):
        return self.aplicar(lambda x, y: (x + dx, y + dy))

    def escalar(self, k):
        cx, cy = self.centro()
        return self.aplicar(lambda x, y: (cx + k * (x - cx),
                                          cy + k * (y - cy)))

    def pintar(self, color):
        for f in self.familia():
            f.color = color
        return self

    def __repr__(self):
        cx, cy = self.centro()
        nombre = type(self).__name__
        return f"{nombre}({self.color}, ({cx:.1f}, {cy:.1f}))"


class Circulo(Figura):
    def __init__(self, radio=1.0, color="rojo"):
        self.radio = radio             # antes de super(): lo usa
        super().__init__(color=color)  # generar_puntos()

    def generar_puntos(self):
        n = 40
        self.puntos = [(self.radio * math.cos(2 * math.pi * k / n),
                        self.radio * math.sin(2 * math.pi * k / n))
                       for k in range(n)]


class Rectangulo(Figura):
    def __init__(self, ancho=4.0, alto=2.0, color="blanco"):
        self.ancho, self.alto = ancho, alto
        super().__init__(color=color)

    def generar_puntos(self):
        a, b = self.ancho / 2, self.alto / 2
        self.puntos = [(-a, -b), (a, -b), (a, b), (-a, b)]


class Cuadrado(Rectangulo):
    def __init__(self, lado=2.0, color="azul"):
        super().__init__(ancho=lado, alto=lado, color=color)


class Grupo(Figura):
    """Una figura que contiene figuras (el papel de VGroup)."""

    def __init__(self, *figuras):
        super().__init__()
        self.agregar(*figuras)

    def agregar(self, *figuras):
        self.subfiguras.extend(figuras)
        return self

    def __len__(self):
        return len(self.subfiguras)

    def __getitem__(self, indice):
        return self.subfiguras[indice]

    def __iter__(self):
        return iter(self.subfiguras)

    def __add__(self, otra):
        return Grupo(*self.subfiguras, otra)

    def ordenar(self, separacion=0.5):
        """Coloca las subfiguras en fila, de izquierda a derecha."""
        x_actual = None
        for f in self:
            x0, x1, _, _ = f.limites()
            if x_actual is not None:
                f.desplazar(x_actual + separacion - x0, 0)
            x_actual = f.limites()[1]
        cx, cy = self.centro()
        return self.desplazar(-cx, -cy)

    def __repr__(self):
        return f"Grupo de {len(self)} figuras"


def suave(t):
    """Función de ritmo: arranca y frena despacio (como smooth)."""
    return 3 * t**2 - 2 * t**3


class Animacion:
    """Cambia una figura con el tiempo (el papel de Animation)."""

    def __init__(self, figura, duracion=1.0, ritmo=suave):
        self.figura = figura
        self.duracion = duracion
        self.ritmo = ritmo

    def iniciar(self):
        """Se llama una vez, antes del primer fotograma."""

    def interpolar(self, alfa):
        """alfa va de 0 a 1. Cada subclase decide qué significa."""
        raise NotImplementedError

    def terminar(self):
        self.interpolar(1.0)

    def __repr__(self):
        nombre = type(self.figura).__name__
        return f"{type(self).__name__}({nombre})"


class Crear(Animacion):
    def interpolar(self, alfa):
        for f in self.figura.familia():
            f.visible = alfa


class Desplazar(Animacion):
    def __init__(self, figura, dx, dy, **opciones):
        super().__init__(figura, **opciones)
        self.dx, self.dy = dx, dy

    def iniciar(self):
        # Guardamos el estado inicial para interpolar desde él
        self.inicio = [f.puntos[:] for f in self.figura.familia()]

    def interpolar(self, alfa):
        ddx, ddy = alfa * self.dx, alfa * self.dy
        for f, pts in zip(self.figura.familia(), self.inicio):
            f.puntos = [(x + ddx, y + ddy) for x, y in pts]


class Escena:
    """Lienzo y director de orquesta (el papel de Scene)."""
    fps = 10
    columnas, filas = 57, 13         # la terminal: 14 × 6 unidades

    def __init__(self):
        self.figuras = []
        self.tiempo = 0.0
        self.fotogramas = 0

    def agregar(self, *figuras):
        for f in figuras:
            if f not in self.figuras:
                self.figuras.append(f)

    def reproducir(self, *animaciones):
        duracion = max(a.duracion for a in animaciones)
        for a in animaciones:
            self.agregar(a.figura)
            a.iniciar()
        n = round(duracion * self.fps)
        for k in range(1, n + 1):
            for a in animaciones:   # polimorfismo: cada animación
                a.interpolar(a.ritmo(k / n))   # sabe interpolarse
            self.fotogramas += 1
        for a in animaciones:
            a.terminar()
        self.tiempo += duracion
        nombres = ", ".join(repr(a) for a in animaciones)
        print(f"  t = {self.tiempo:3.1f} s   reproducir({nombres})")

    def esperar(self, segundos=1.0):
        self.tiempo += segundos
        self.fotogramas += round(segundos * self.fps)

    def preparar(self):
        """Gancho que se ejecuta antes de construir()."""

    def construir(self):
        """Gancho: aquí va la animación (se sobrescribe)."""

    def render(self):
        print(f"Renderizando {type(self).__name__}")
        self.preparar()
        self.construir()
        print(f"{self.fotogramas} fotogramas, {self.tiempo:.1f} s")
        self.dibujar()

    # --- Dibujo en la terminal: x en [-7, 7], y en [-3, 3] -----
    def dibujar(self):
        lienzo = [[" "] * self.columnas for _ in range(self.filas)]
        for figura in self.figuras:
            for f in figura.familia():
                self._trazar(f, lienzo)
        borde = "+" + "-" * self.columnas + "+"
        print(borde)
        for fila in lienzo:
            print("|" + "".join(fila) + "|")
        print(borde)

    def _trazar(self, f, lienzo):
        n = len(f.puntos)
        tramos = n if len(f.puntos) > 2 else n - 1
        for i in range(round(tramos * f.visible)):
            (x0, y0), (x1, y1) = f.puntos[i], f.puntos[(i + 1) % n]
            for paso in range(21):
                t = paso / 20
                x, y = x0 + t * (x1 - x0), y0 + t * (y1 - y0)
                c = round((x + 7) * 4)
                r = round((3 - y) * 2)
                if 0 <= c < self.columnas and 0 <= r < self.filas:
                    lienzo[r][c] = CARACTER.get(f.color, "?")
