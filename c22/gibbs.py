import numpy as np
from scipy.special import sici


def suma_parcial(x, N):
    n = np.arange(1, N + 1, 2)[:, None]      # impares, en columna
    return 4 / np.pi * np.sum(np.sin(n * x) / n, axis=0)


x = np.linspace(1e-6, np.pi / 2, 200001)
print("   N     máx S_N   dónde     pi/(N+1)")
for N in (9, 19, 49, 99, 199, 999):
    S = suma_parcial(x, N)
    k = np.argmax(S)
    teoria = np.pi / (N + 1)
    print(f"{N:4d}   {S[k]:.6f}   {x[k]:.5f}   {teoria:.5f}")
limite = 2 / np.pi * sici(np.pi)[0]           # (2/pi) Si(pi)
print(f"límite (2/pi) Si(pi) = {limite:.6f}")
print(f"sobrepaso: {(limite - 1) / 2:.2%} del salto (que vale 2)")
