import numpy as np

w = -16 + 0j                        # resolvemos z^4 = -16
n = 4
modulo, arg = abs(w) ** (1 / n), np.angle(w)
k = np.arange(n)
raices = modulo * np.exp(1j * (arg + 2 * np.pi * k) / n)
print(np.round(raices, 4))
print("¿z^4 = -16?", np.allclose(raices**4, w))
print("comparación con np.roots:",
      np.allclose(sorted(raices, key=np.angle),
                  sorted(np.roots([1, 0, 0, 0, 16]), key=np.angle)))
