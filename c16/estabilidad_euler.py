# Oscilador x'' = -x con x(0) = 1, v(0) = 0: energía exacta 0.5
def simular(h, T, metodo):
    x, v = 1.0, 0.0
    for _ in range(round(T / h)):
        if metodo == "explicito":          # usa la velocidad vieja
            x, v = x + h * v, v - h * x
        else:                              # semi-implícito:
            v = v - h * x                  # primero la velocidad
            x = x + h * v                  # y con ella, la posición
    return 0.5 * (x * x + v * v)


print("Energía en t = 20")
print("   h    Euler explícito   semi-implícito")
for h in [0.5, 0.1, 0.01, 1.9, 2.1]:
    print(f"{h:5}  {simular(h, 20, 'explicito'):16.4g}"
          f"  {simular(h, 20, 'semi'):15.4g}")
