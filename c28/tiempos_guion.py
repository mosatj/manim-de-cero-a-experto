# Escaleta de tiempos: cuánto dura cada bloque leído en voz alta
from guion_impares import GUION, duracion


def mmss(segundos):
    return f"{int(segundos // 60)}:{round(segundos % 60):02d}"


inicio = 0.0
print(f"{'bloque':<16}{'palabras':>9}{'duración':>10}{'entra en':>10}")
for b in GUION:
    d = duracion(b)
    print(f"{b['bloque']:<16}{len(b['voz'].split()):>9}"
          f"{d:>9.1f}s{mmss(inicio):>10}")
    inicio += d
print(f"{'total':<16}{'':>9}{inicio:>9.1f}s{mmss(inicio):>10}")
