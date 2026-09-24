import numpy as np

lista = [1, 2, 3]
arreglo = np.array([1, 2, 3])
print("lista + lista     :", lista + lista)      # concatena
print("arreglo + arreglo :", arreglo + arreglo)  # suma uno a uno
print("lista * 2         :", lista * 2)          # repite
print("arreglo * 2       :", arreglo * 2)        # multiplica
print("arreglo ** 2      :", arreglo**2)

p = np.array([2.5, -1, 0])
print("p =", p, "| tipo:", p.dtype, "| forma:", p.shape)
print("p[0] =", p[0], "| p[:2] =", p[:2])
m = np.array([[1, 2, 3], [4, 5, 6]])
print("m.shape =", m.shape, "| m.ndim =", m.ndim, "| m[1, 2] =",
      m[1, 2])
