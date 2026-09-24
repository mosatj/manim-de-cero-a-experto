# Propuesto: usar nuestro módulo de conversiones
from conversiones import a_grados, a_radianes

for g in [30, 45, 90]:
    print(f"{g}° = {a_radianes(g):.4f} rad")
print(f"1 rad = {a_grados(1):.4f}°")
