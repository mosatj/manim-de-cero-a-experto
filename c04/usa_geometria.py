# Tres formas de importar nuestro propio módulo
import geometria
from geometria import distancia
import geometria as geo

print(geometria.area_circulo(2))
print(distancia((1, 1), (4, 5)))
print(geo.PI)
print("Nombre del módulo:", geometria.__name__)
print("Nombre de este programa:", __name__)
