# Genera los subtítulos (formato SRT) de la lección a partir del guion
from guion_impares import GUION, duracion
from subtitulos import repartir, marca_srt

entradas, t = [], 0.0
for bloque in GUION:
    d = duracion(bloque)
    entradas += repartir(bloque["voz"], t, d - 1.0)  # sin el respiro
    t += d

srt = []
for n, (ini, fin, texto) in enumerate(entradas, start=1):
    srt.append(f"{n}\n{marca_srt(ini)} --> {marca_srt(fin)}\n{texto}\n")

with open("leccion_impares.srt", "w", encoding="utf-8") as archivo:
    archivo.write("\n".join(srt))
print("\n".join(srt[:3]))
print(f"... {len(srt)} subtítulos en leccion_impares.srt")
