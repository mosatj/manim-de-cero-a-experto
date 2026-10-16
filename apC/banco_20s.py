from manim import *


class Banco20s(Scene):
    """Escena de referencia de 20 s para medir tiempos de render: mezcla
    lo que hace un vídeo típico (texto, fórmula, ejes, gráfica,
    transformación y un actualizador)."""

    def construct(self):
        titulo = Text("Área bajo una parábola", font_size=48).to_edge(UP)
        self.play(Write(titulo), run_time=2)                       # 2 s
        ejes = Axes(x_range=[0, 3, 1], y_range=[0, 9, 3],
                    x_length=7, y_length=4.5).shift(DOWN * 0.6)
        curva = ejes.plot(lambda x: x**2, color=BLUE)
        self.play(Create(ejes), Create(curva), run_time=3)          # 5 s
        rect = ejes.get_riemann_rectangles(curva, x_range=[0, 3],
                                           dx=0.5, fill_opacity=0.6)
        self.play(Create(rect), run_time=2)                         # 7 s
        finos = ejes.get_riemann_rectangles(curva, x_range=[0, 3],
                                            dx=0.1, fill_opacity=0.6)
        self.play(Transform(rect, finos), run_time=3)               # 10 s
        formula = MathTex(r"\int_0^3 x^2\,dx = 9", font_size=44)
        formula.to_corner(UR).shift(DOWN * 0.9)
        self.play(Write(formula), run_time=2)                       # 12 s
        x = ValueTracker(0.2)
        punto = always_redraw(lambda: Dot(
            ejes.c2p(x.get_value(), x.get_value() ** 2), color=RED))
        self.add(punto)
        self.play(x.animate.set_value(2.9), run_time=5)             # 17 s
        self.play(Indicate(formula), run_time=1.5)                  # 18,5 s
        self.wait(1.5)                                              # 20 s


def recurso(nombre):
    """Crea, la primera vez, una imagen o un sonido de prueba junto al
    archivo (así el banco no depende de archivos externos)."""
    from pathlib import Path
    ruta = Path(__file__).with_name(nombre)
    if ruta.exists():
        return str(ruta)
    if nombre.endswith(".png"):
        from PIL import Image
        alto, ancho = 1080, 1920
        y, x = np.mgrid[0:alto, 0:ancho] / [alto, ancho][0]
        ruido = np.random.default_rng(1).random((alto, ancho))
        r = (0.5 + 0.5 * np.sin(9 * x + 3 * y)) * 200 + 40 * ruido
        g = (0.5 + 0.5 * np.cos(7 * y - 2 * x)) * 160 + 40 * ruido
        b = 120 + 80 * np.sin(5 * (x + y)) + 40 * ruido
        Image.fromarray(np.clip(np.dstack([r, g, b]), 0, 255)
                        .astype(np.uint8)).save(ruta)
    else:  # pista de 20 s: acordes suaves a 44,1 kHz
        import wave
        t = np.arange(0, 20, 1 / 44100)
        onda = sum(np.sin(2 * np.pi * f * t) for f in (220, 277, 330))
        onda *= 0.2 * (1 + np.sin(2 * np.pi * 0.25 * t)) / 2
        with wave.open(str(ruta), "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(44100)
            w.writeframes((onda * 32767 / 3).astype(np.int16).tobytes())
    return str(ruta)


class BancoImagen(Banco20s):
    """La misma escena con una fotografía de 1920 × 1080 que se mueve y
    se escala detrás: los mapas de bits cuestan más que los vectores."""

    def construct(self):
        foto = ImageMobject(recurso("foto_prueba.png"))
        foto.set(height=config.frame_height).set_opacity(0.35)
        foto.add_updater(lambda m, dt: m.scale(1 + 0.01 * dt))
        self.add(foto)
        super().construct()


class BancoSonido(Banco20s):
    """La misma escena con una pista de audio de 20 s."""

    def construct(self):
        self.add_sound(recurso("pista_prueba.wav"))
        super().construct()


class Banco3D(ThreeDScene):
    """Una superficie sombreada y la cámara orbitando durante 20 s."""

    def construct(self):
        self.set_camera_orientation(phi=65 * DEGREES, theta=30 * DEGREES)
        ejes = ThreeDAxes(x_range=[-3, 3], y_range=[-3, 3],
                          z_range=[-1, 2])
        superficie = Surface(
            lambda u, v: ejes.c2p(u, v, 1.5 * np.exp(-(u**2 + v**2) / 2)),
            u_range=[-3, 3], v_range=[-3, 3], resolution=(24, 24),
            fill_opacity=0.8)
        superficie.set_fill_by_value(axes=ejes, colorscale=[BLUE, RED],
                                     axis=2)
        self.play(Create(ejes), run_time=2)
        self.play(Create(superficie), run_time=3)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(15)


class BancoDenso(Scene):
    """2000 puntos que se mueven a la vez: muchos objetos por fotograma."""

    def construct(self):
        rng = np.random.default_rng(2)
        puntos = VGroup(*[Dot(radius=0.03, color=BLUE).move_to(
            [rng.uniform(-7, 7), rng.uniform(-4, 4), 0])
            for _ in range(2000)])
        self.play(FadeIn(puntos), run_time=2)
        self.play(Rotate(puntos, PI, about_point=ORIGIN), run_time=8)
        self.play(puntos.animate.scale(0.4), run_time=5)
        self.play(puntos.animate.set_color(RED).scale(2.2), run_time=5)
