# Genera datos SINTÉTICOS (inventados, pero reproducibles) de un
# estudio ficticio: horas de estudio semanales y nota (escala 0-20).
import csv
import os
import numpy as np

rng = np.random.default_rng(20260923)          # semilla fija
n = 40
horas = rng.uniform(0.5, 10, n).round(1)
ruido = rng.normal(0, 1.8, n)
nota = (5 + 1.3 * horas + ruido).clip(0, 20).round(1)

# Se escribe en un archivo temporal y luego se renombra: así nadie
# lee nunca un CSV a medio escribir.
with open("estudio.tmp", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["horas", "nota"])
    escritor.writerows(zip(horas.tolist(), nota.tolist()))
os.replace("estudio.tmp", "estudio.csv")

print(f"Filas escritas: {n}")
print("Primeras filas:",
      list(zip(horas.tolist()[:3], nota.tolist()[:3])))
