from manim import *

# Fotograma sobre fondo claro que se imprime con sus colores reales
# (la luz no puede invertirse). Cada esfera se sombrea píxel a píxel
# con el modelo de Lambert: brillo = intensidad * max(0, normal · luz).
LUCES = {  # dirección (x, y, z: z sale hacia el espectador) e intensidad
    "principal": (np.array([-1.0, 0.9, 0.9]), 1.00),
    "relleno": (np.array([1.0, 0.1, 0.8]), 0.35),
    "contraluz": (np.array([0.5, 0.6, -0.8]), 1.60),
}
COLOR_OBJETO = np.array([0.31, 0.49, 0.60])  # azul acero del libro
FONDO = np.array([0.93, 0.91, 0.87])         # marfil


def esfera(luces, lado=360):
    t = np.linspace(-1.15, 1.15, lado)
    x, y = np.meshgrid(t, -t)
    r2 = x**2 + y**2
    dentro = r2 <= 1
    z = np.sqrt(np.clip(1 - r2, 0, None))
    normal = np.stack([x, y, z], axis=-1)
    brillo = np.full(x.shape, 0.06)  # luz ambiente mínima
    borde = np.zeros(x.shape)        # el contraluz ilumina el contorno
    for nombre in luces:
        direccion, intensidad = LUCES[nombre]
        d = direccion / np.linalg.norm(direccion)
        aporte = intensidad * np.clip(normal @ d, 0, None)
        if nombre == "contraluz":
            borde += aporte
        else:
            brillo += aporte
    color = brillo[..., None] * COLOR_OBJETO * 1.5
    color = np.clip(color + borde[..., None] * 0.9, 0, 1)  # luz blanca
    sombra = np.clip(1 - 0.25 * np.exp(-((x - 0.25)**2 + (y + 1.05)**2)
                                       * 6), 0, 1)
    imagen = np.where(dentro[..., None], color, FONDO * sombra[..., None])
    return ImageMobject((imagen * 255).astype(np.uint8)).set(height=3.0)


class IluminacionTresPuntos(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        casos = [
            (["principal"], "1. principal"),
            (["principal", "relleno"], "2. + relleno"),
            (["principal", "relleno", "contraluz"], "3. + contraluz"),
            (["contraluz"], "solo contraluz"),
        ]
        paneles = Group()
        for luces, nombre in casos:
            rotulo = Text(nombre, font_size=28, color=BLACK)
            paneles.add(Group(esfera(luces), rotulo).arrange(DOWN,
                                                             buff=0.25))
        paneles.arrange(RIGHT, buff=0.35).to_edge(UP, buff=0.45)

        # Planta del montaje: la cámara abajo, el objeto en el centro
        objeto = Circle(radius=0.35, color=BLUE_E, fill_opacity=1)
        camara = Text("cámara", font_size=24, color=BLACK)
        camara.next_to(objeto, DOWN, buff=0.85)
        planta = VGroup(objeto, camara)
        for nombre, (direccion, _) in LUCES.items():
            # En planta: x a la derecha; hacia la cámara (z > 0) es abajo
            u = normalize(np.array([direccion[0], -direccion[2], 0]))
            foco = Square(side_length=0.28, color=RED_E,
                          fill_opacity=1).move_to(objeto.get_center()
                                                  + 1.55 * u)
            haz = Arrow(foco.get_center(), objeto.get_center() + 0.4 * u,
                        buff=0.18, color=RED_E, stroke_width=4)
            etiqueta = Text(nombre, font_size=24, color=BLACK)
            etiqueta.next_to(foco, u, buff=0.12)
            planta.add(foco, haz, etiqueta)
        planta.add(Arrow(camara.get_top(), objeto.get_bottom(), buff=0.1,
                         color=GREY_D, stroke_width=3))
        planta.scale(0.95).next_to(paneles, DOWN, buff=0.35)
        titulo = Text("vista desde arriba", font_size=22, color=GREY_D)
        titulo.next_to(planta, LEFT, buff=0.5)
        self.add(paneles, planta, titulo)
