# Propuesto: tabla de grados a radianes
pi = 3.141592653589793
for grados in [0, 30, 45, 60, 90, 180, 360]:
    radianes = grados * pi / 180
    print(f"{grados:>4}° = {radianes:.4f} rad")
