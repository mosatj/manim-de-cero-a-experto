import math
import time
import numpy as np

n = 1_000_000
x = np.linspace(0, 10, n)

inicio = time.perf_counter()
con_bucle = [math.sin(v) for v in x]        # un valor cada vez
t_bucle = time.perf_counter() - inicio

inicio = time.perf_counter()
vectorizado = np.sin(x)                 # todo el arreglo de una vez
t_vector = time.perf_counter() - inicio

print(f"bucle: {t_bucle * 1000:.0f} ms | "
      f"NumPy: {t_vector * 1000:.1f} ms")
print(f"NumPy fue unas {t_bucle / t_vector:.0f} veces más rápido")
print("¿mismo resultado?", np.allclose(con_bucle, vectorizado))
