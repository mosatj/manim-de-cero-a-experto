# R_n: valor de r con un ciclo superestable de periodo 2^n
# (x = 1/2 pertenece al ciclo): g(r) = f_r^(2^n)(1/2) - 1/2 = 0


def g(r, n):
    x = 0.5
    for _ in range(2**n):
        x = r * x * (1 - x)
    return x - 0.5


def newton(r, n, tol=1e-13):
    for _ in range(100):
        d = 1e-9
        paso = g(r, n) / ((g(r + d, n) - g(r - d, n)) / (2 * d))
        r -= paso
        if abs(paso) < tol:
            break
    return r


R = [2.0, 1 + 5**0.5]                     # R_0 y R_1 exactos
for n in range(2, 11):
    # predicción geométrica del siguiente valor (razón inicial 4)
    delta = 4.0 if n == 2 else (R[-2] - R[-3]) / (R[-1] - R[-2])
    R.append(newton(R[-1] + (R[-1] - R[-2]) / delta, n))
for n in range(2, len(R)):
    razon = (R[n - 1] - R[n - 2]) / (R[n] - R[n - 1])
    print(f"n = {n:2d}   R_n = {R[n]:.10f}   razón = {razon:.6f}")
