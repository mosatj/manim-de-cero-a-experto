# Utilidades para subtítulos (Python puro): trocear el texto de la voz
# en rótulos legibles y repartir el tiempo entre ellos.
import re


def lineas(frase, max_car):
    """Parte una frase en líneas de hasta max_car caracteres."""
    resultado, actual = [], ""
    for palabra in frase.split():
        if actual and len(actual) + 1 + len(palabra) > max_car:
            resultado.append(actual)
            actual = palabra
        else:
            actual = f"{actual} {palabra}".strip()
    return resultado + [actual]


def trozos(texto, max_car=40, max_lineas=2):
    """Rótulos de hasta max_lineas líneas; nunca mezclan dos frases."""
    rotulos = []
    for frase in re.split(r"(?<=[.?!])\s+", texto.strip()):
        partes = lineas(frase, max_car)
        rotulos += ["\n".join(partes[i:i + max_lineas])
                    for i in range(0, len(partes), max_lineas)]
    return rotulos


def repartir(texto, inicio, duracion):
    """(inicio, fin, rótulo) con tiempo proporcional a los caracteres."""
    rotulos = trozos(texto)
    total = sum(len(r) for r in rotulos)
    t, salida = inicio, []
    for r in rotulos:
        d = duracion * len(r) / total
        salida.append((t, t + d, r))
        t += d
    return salida


def marca_srt(segundos):
    """12.5 -> '00:00:12,500' (formato de tiempo de SubRip)."""
    ms = round(segundos * 1000)
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
