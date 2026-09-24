from manim import *
from funcion import f, fx, fy, semiejes

COLOR_X, COLOR_Y, COLOR_NIVEL = "#E0B04A", "#B04A5A", "#6FA3C0"
R = 2.2  # borde de la «colina»: la curva de nivel f = 4 - R^2


def ejes3d():
    return ThreeDAxes(
        x_range=[-3.5, 3.5, 1],
        y_range=[-2.5, 2.5, 1],
        z_range=[-1, 4, 1],
        x_length=7,
        y_length=5,
        z_length=3.5,
    )


def superficie(ejes, opacidad=0.6):
    # Coordenadas «elípticas»: x = sqrt(2) u cos v, y = u sin v.
    # Así el borde de la superficie es una curva de nivel y no
    # un rectángulo
    s = Surface(
        lambda u, v: ejes.c2p(
            np.sqrt(2) * u * np.cos(v), u * np.sin(v), 4 - u**2
        ),
        u_range=[0, R],
        v_range=[0, TAU],
        resolution=(12, 32),
        fill_opacity=opacidad,
        stroke_width=0.3,
    )
    # Color según la altura z: de azul (bajo) a crema (alto)
    return s.set_fill_by_value(
        axes=ejes,
        colorscale=[
            ("#1F4E6B", -1),
            ("#6FA3C0", 1.5),
            ("#E9F2F7", 4),
        ],
        axis=2,
    )


def curva_nivel(ejes, c, altura=None):
    """Elipse f = c a la altura z = c (o a la que se pida)."""
    sx, sy = semiejes(c)
    z = c if altura is None else altura
    return ParametricFunction(
        lambda t: ejes.c2p(sx * np.cos(t), sy * np.sin(t), z),
        t_range=[0, TAU],
        color=COLOR_NIVEL,
        stroke_width=4,
    )


def corte(ejes, a, b, direccion, color):
    """Curva que deja en la superficie el plano y = b (dir. 'x')
    o x = a (dirección 'y')."""
    if direccion == "x":
        tope = np.sqrt(2 * (R**2 - b**2))  # dónde el plano sale
        return ParametricFunction(
            lambda t: ejes.c2p(t, b, f(t, b)),
            t_range=[-tope, tope],
            color=color,
            stroke_width=5,
        )
    tope = np.sqrt(R**2 - a**2 / 2)
    return ParametricFunction(
        lambda t: ejes.c2p(a, t, f(a, t)),
        t_range=[-tope, tope],
        color=color,
        stroke_width=5,
    )


def tangente(ejes, a, b, direccion, color, largo=1.2):
    """Tangente al corte: su pendiente es la derivada parcial."""
    z = f(a, b)
    if direccion == "x":
        d = np.array([1, 0, fx(a, b)])
    else:
        d = np.array([0, 1, fy(a, b)])
    d = d / np.linalg.norm(d) * largo
    p = np.array([a, b, z])
    return Line3D(
        ejes.c2p(*(p - d)),
        ejes.c2p(*(p + d)),
        color=color,
        thickness=0.03,
    )


def plano_corte(ejes, a, b, direccion, color):
    """Rectángulo translúcido del plano vertical que corta."""
    if direccion == "x":
        esquinas = [
            (-3.3, b, -1),
            (3.3, b, -1),
            (3.3, b, 4),
            (-3.3, b, 4),
        ]
    else:
        esquinas = [
            (a, -2.4, -1),
            (a, 2.4, -1),
            (a, 2.4, 4),
            (a, -2.4, 4),
        ]
    return Polygon(
        *[ejes.c2p(*e) for e in esquinas],
        stroke_width=1,
        color=color,
        fill_opacity=0.18,
    )
