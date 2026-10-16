# Prueba del modelo antes de animarlo: ¿las operaciones son las
# correctas y la solución coincide con la de NumPy?
import numpy as np
from eliminacion import gauss_jordan, operacion
from sistema import AMPLIADA, COLUMNAS_A

operaciones = 0
for evento in gauss_jordan(AMPLIADA, COLUMNAS_A):
    if evento[0] == "pivote":
        _, i, j = evento
        print(f"pivote: fila {i + 1}, columna {j + 1}")
    elif evento[0] == "fin":
        reducida = evento[1]
    else:
        operaciones += 1
        print("   ", operacion(evento, numero=str, flecha="<-"))
solucion = [float(fila[-1]) for fila in reducida]
A = np.array(AMPLIADA, dtype=float)
esperada = np.linalg.solve(A[:, :COLUMNAS_A], A[:, COLUMNAS_A])
assert np.allclose(solucion, esperada)
print("operaciones elementales:", operaciones)
print("solución:", solucion, " NumPy:", esperada)
