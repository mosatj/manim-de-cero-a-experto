# El algoritmo como generador: trabaja con fracciones exactas y
# no dibuja nada, solo anuncia cada operación elemental con yield
from fractions import Fraction


def gauss_jordan(ampliada, columnas):
    """Reduce [A | B] por filas; A ocupa las primeras `columnas`.
    Eventos: ('pivote', i, j); ('intercambiar', i, k, m),
    ('escalar', i, factor, m) y ('eliminar', i, k, factor, m),
    que significa fila i <- fila i - factor * fila k, donde m es
    la matriz resultante; ('incompatible', i) y ('fin', m)."""
    m = [[Fraction(x) for x in fila] for fila in ampliada]
    n = len(m)
    fila = 0  # siguiente fila donde colocar un pivote
    for j in range(columnas):
        k = next((i for i in range(fila, n) if m[i][j]), None)
        if k is None:
            continue  # columna sin pivote: se salta
        if k != fila:
            m[fila], m[k] = m[k], m[fila]
            yield ("intercambiar", fila, k, copia(m))
        yield ("pivote", fila, j)
        if m[fila][j] != 1:
            factor = 1 / m[fila][j]
            m[fila] = [factor * x for x in m[fila]]
            yield ("escalar", fila, factor, copia(m))
        for i in range(n):
            if i != fila and m[i][j] != 0:
                f = m[i][j]
                m[i] = [x - f * y for x, y in zip(m[i], m[fila])]
                yield ("eliminar", i, fila, f, copia(m))
        fila += 1
    for i in range(n):  # fila 0 0 ... 0 | c con c distinto de 0
        if not any(m[i][:columnas]) and any(m[i][columnas:]):
            yield ("incompatible", i)
    yield ("fin", m)


def copia(m):
    return [list(fila) for fila in m]


def como_latex(x):
    """Una fracción como texto de LaTeX: enteros sin barra."""
    if x.denominator == 1:
        return str(x.numerator)
    signo = "-" if x < 0 else ""
    num, den = abs(x.numerator), x.denominator
    return rf"{signo}\tfrac{{{num}}}{{{den}}}"


def operacion(evento, numero=como_latex, flecha=r"\leftarrow"):
    """El rótulo R_i <- R_i - 2 R_k de un evento, o None. Con
    numero=str y flecha='<-' sale texto plano para la terminal."""
    tipo = evento[0]
    if tipo == "escalar":
        _, i, f, _ = evento
        return rf"R_{i + 1} {flecha} {numero(f)} R_{i + 1}"
    if tipo == "eliminar":
        _, i, k, f, _ = evento
        signo = "+" if f < 0 else "-"
        coef = "" if abs(f) == 1 else numero(abs(f))
        return (rf"R_{i + 1} {flecha} R_{i + 1} "
                rf"{signo} {coef}R_{k + 1}")
    if tipo == "intercambiar":
        _, i, k, _ = evento
        return rf"R_{i + 1} \leftrightarrow R_{k + 1}"
    return None
