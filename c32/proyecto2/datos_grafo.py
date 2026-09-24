# Modelo: los datos del grafo, sin nada de Manim
VERTICES = ["A", "B", "C", "D", "E", "F"]
ARISTAS = {  # (u, v): peso; el grafo no es dirigido
    ("A", "B"): 4,
    ("A", "C"): 2,
    ("B", "C"): 1,
    ("B", "D"): 5,
    ("C", "D"): 8,
    ("C", "E"): 10,
    ("D", "E"): 2,
    ("D", "F"): 6,
    ("E", "F"): 5,
}
POSICIONES = {  # coordenadas de pantalla (x, y, z)
    "A": (-4.5, 0, 0),
    "B": (-1.6, 2, 0),
    "C": (-1.6, -2, 0),
    "D": (1.6, 2, 0),
    "E": (1.6, -2, 0),
    "F": (4.5, 0, 0),
}
ORIGEN = "A"
