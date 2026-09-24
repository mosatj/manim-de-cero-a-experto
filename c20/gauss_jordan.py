"""Eliminación de Gauss-Jordan con aritmética exacta (sin Manim).

gauss_jordan(M, columnas) devuelve la lista de pasos
[(operación, matriz, pivote)], empezando por (None, M, None).
Solo se buscan pivotes en las primeras «columnas» columnas (las de A
en una matriz aumentada [A | b] o [A | I]).
"""
from fractions import Fraction


def copiar(M):
    return [fila[:] for fila in M]


def gauss_jordan(M, columnas=None):
    M = [[Fraction(x) for x in fila] for fila in M]
    m = len(M)
    columnas = len(M[0]) if columnas is None else columnas
    pasos = [(None, copiar(M), None)]
    fila = 0                           # fila del próximo pivote
    for col in range(columnas):
        candidatas = [i for i in range(fila, m) if M[i][col] != 0]
        if not candidatas:                    # columna sin pivote
            continue
        # Preferimos un 1 (o −1) como pivote: evita fracciones
        unos = [i for i in candidatas if abs(M[i][col]) == 1]
        p = unos[0] if unos else candidatas[0]
        if p != fila:
            M[fila], M[p] = M[p], M[fila]
            op = ("intercambio", fila, p)
            pasos.append((op, copiar(M), None))
        if M[fila][col] != 1:
            c = 1 / M[fila][col]
            M[fila] = [c * x for x in M[fila]]
            op = ("escala", fila, c)
            pasos.append((op, copiar(M), (fila, col)))
        for i in range(m):
            if i != fila and M[i][col] != 0:
                c = M[i][col]
                M[i] = [x - c * y for x, y in zip(M[i], M[fila])]
                pasos.append((("resta", i, c, fila), copiar(M),
                              (fila, col)))
        fila += 1
        if fila == m:
            break
    return pasos


def tex(x):
    """Fracción en LaTeX: 3, -2, \\tfrac{2}{3}, -\\tfrac{5}{3}."""
    x = Fraction(x)
    if x.denominator == 1:
        return str(x.numerator)
    signo = "-" if x < 0 else ""
    p, q = abs(x.numerator), x.denominator
    return rf"{signo}\tfrac{{{p}}}{{{q}}}"


def operacion(op, latex=False):
    """Operación elemental en notación del libro (F1, F2, ...)."""
    if op is None:
        return ""
    sub = "_" if latex else ""
    F = lambda i: f"F{sub}{i + 1}"
    num = tex if latex else str
    flecha = r"\leftarrow " if latex else "<- "
    if op[0] == "intercambio":
        doble = r"\leftrightarrow " if latex else " <-> "
        return F(op[1]) + doble + F(op[2])
    if op[0] == "escala":
        c = num(op[2]) if latex else f"({op[2]})"
        return f"{F(op[1])} {flecha}{c}{F(op[1])}"
    _, i, c, j = op
    signo = "-" if c > 0 else "+"
    coef = "" if abs(c) == 1 else num(abs(c))
    return f"{F(i)} {flecha}{F(i)} {signo} {coef}{F(j)}"


if __name__ == "__main__":
    # Sistema: y − z = −1,  2x + y + 2z = 10,  x − y = −1
    aumentada = [[0, 1, -1, -1], [2, 1, 2, 10], [1, -1, 0, -1]]
    pasos = gauss_jordan(aumentada, columnas=3)
    for op, _, _ in pasos[1:]:
        print(operacion(op))
    print("Forma escalonada reducida:")
    for fila in pasos[-1][1]:
        print("   ", "  ".join(f"{str(x):>3}" for x in fila))
