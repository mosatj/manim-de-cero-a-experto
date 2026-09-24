import numpy as np

z = 3 + 4j                            # j es la unidad imaginaria
print("z =", z, "| real:", z.real, "| imag:", z.imag)
argumento = np.degrees(np.angle(z))       # en grados
print("|z| =", abs(z), "| arg(z) =", round(argumento, 2),
      "° | conjugado:", z.conjugate())

# Multiplicar por e^{iθ} gira θ sin cambiar el módulo
giro = np.exp(1j * np.pi / 2)         # e^{iπ/2} = i
print("e^{iπ/2} =", np.round(giro, 10))
print("z · i =", z * 1j, "| |z·i| =", abs(z * 1j))
print("identidad de Euler: e^{iπ} + 1 =", np.exp(1j * np.pi) + 1)

# Las 6 raíces sextas de la unidad, de una sola vez
k = np.arange(6)
raices = np.exp(2j * np.pi * k / 6)
print("raíces:", np.round(raices, 3))
print("¿r^6 = 1 para todas?", np.allclose(raices**6, 1))
