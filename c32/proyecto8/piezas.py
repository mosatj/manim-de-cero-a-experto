from manim import *
from funcion import f, A, B, particion, volumen_exacto
from estilo import COLOR_CURVA, COLOR_SOLIDO, COLOR_DISCO
from estilo import COLOR_ACENTO, TAM_ROTULO

# --- Piezas planas ----------------------------------------------


def ejes2d():
    # Misma escala en x y en y: las elipses de los discos no se
    # deforman y la región se ve con sus proporciones reales
    return Axes(
        x_range=[0, 4.5, 1],
        y_range=[-1.8, 1.8, 1],
        x_length=6.75,
        y_length=5.4,
        tips=False,
        axis_config={"stroke_width": 2},
    )


def curva(ejes, espejo=False):
    """La gráfica de f o, con espejo, la de -f (el otro borde)."""
    signo = -1 if espejo else 1
    return ejes.plot(
        lambda x: signo * f(x),
        x_range=[A, B],
        color=COLOR_CURVA,
        stroke_width=4,
    )


def region_2d(ejes, grafica):
    return ejes.get_area(
        grafica, x_range=(A, B), color=COLOR_SOLIDO, opacity=0.4
    )


def rectangulos(ejes, grafica, n):
    """n rectángulos de altura f en el punto medio: un disco visto
    de perfil."""
    dx = (B - A) / n
    return ejes.get_riemann_rectangles(
        grafica,
        x_range=[A, B],
        dx=dx,
        input_sample_type="center",
        color=COLOR_DISCO,
        fill_opacity=0.45,
        stroke_color=COLOR_DISCO,
        stroke_width=1,
    )


def discos_2d(ejes, n):
    """Cada disco, insinuado como la elipse que deja al girar."""
    xs, dx = particion(n)
    ancho = 0.6 * (ejes.c2p(dx, 0)[0] - ejes.c2p(0, 0)[0])
    grupo = VGroup()
    for x in xs:
        alto = ejes.c2p(x, f(x))[1] - ejes.c2p(x, -f(x))[1]
        grupo.add(
            Ellipse(
                width=ancho,
                height=alto,
                color=COLOR_DISCO,
                fill_opacity=0.35,
                stroke_width=1.5,
            ).move_to(ejes.c2p(x, 0))
        )
    return grupo


# --- Piezas en el espacio ---------------------------------------


def ejes3d():
    # 1,2 unidades de pantalla por unidad matemática en los tres
    # ejes: así un disco de radio f(x) se construye con esa escala
    return ThreeDAxes(
        x_range=[0, 4.5, 1],
        y_range=[-2, 2, 1],
        z_range=[-2, 2, 1],
        x_length=5.4,
        y_length=4.8,
        z_length=4.8,
    )


def perfil3d(ejes):
    """El perfil z = f(x), de pie en el plano vertical y = 0."""
    return ParametricFunction(
        lambda t: ejes.c2p(t, 0, f(t)),
        t_range=[A, B],
        color=COLOR_CURVA,
        stroke_width=4,
    )


def superficie(ejes, opacidad=0.55):
    """El sólido: cada x da una circunferencia de radio f(x)."""
    return Surface(
        lambda u, v: ejes.c2p(
            u, f(u) * np.cos(v), f(u) * np.sin(v)
        ),
        u_range=[A, B],
        v_range=[0, TAU],
        resolution=(24, 32),
        fill_opacity=opacidad,
        checkerboard_colors=[COLOR_SOLIDO, "#4F7C99"],
        stroke_width=0.3,
        stroke_color=COLOR_SOLIDO,
    )


def discos_3d(ejes, n):
    """n cilindros finos de radio f(x_i) a lo largo del eje x."""
    xs, dx = particion(n)
    escala = ejes.c2p(1, 0, 0)[0] - ejes.c2p(0, 0, 0)[0]
    grupo = VGroup()
    for x in xs:
        disco = Cylinder(
            radius=f(x) * escala,
            height=0.9 * dx * escala,  # un respiro entre discos
            direction=RIGHT,
            resolution=(1, 24),  # el lateral no necesita más
            fill_color=COLOR_DISCO,
            fill_opacity=0.35,
            checkerboard_colors=False,
            stroke_color=COLOR_DISCO,
            stroke_width=1,
        )
        grupo.add(disco.move_to(ejes.c2p(x, 0, 0)))
    return grupo


# --- Rótulos ----------------------------------------------------


def rotulo_discos(n, valor):
    """«n = 8: V ≈ 14,300», con el valor calculado, no escrito."""
    return MathTex(
        rf"n={n}:\quad V\approx{valor:.3f}",
        font_size=TAM_ROTULO,
        color=COLOR_DISCO,
    )


def rotulo_exacto():
    return MathTex(
        rf"V=\pi\int_0^4 f(x)^2\,dx={volumen_exacto():.3f}",
        font_size=TAM_ROTULO,
        color=COLOR_ACENTO,
    )
