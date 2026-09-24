import numpy as np
from metodos_edo import euler, heun, rk4, resolver, f, exacta

print("   h      Euler     Heun      RK4       (error en t = 2)")
anteriores = None
for n in (10, 20, 40, 80, 160):
    h = 2 / n
    errores = [abs(resolver(m, f, 0, 0.5, h, n)[1][-1] - exacta(2))
               for m in (euler, heun, rk4)]
    print(f"{h:.4f}  " + "  ".join(f"{e:.2e}" for e in errores))
    if anteriores:
        # orden observado p = log2(E(2h) / E(h))
        p = [np.log2(a / e) for a, e in zip(anteriores, errores)]
        print("  p ≈   " + "  ".join(f"{x:8.2f}" for x in p))
    anteriores = errores
