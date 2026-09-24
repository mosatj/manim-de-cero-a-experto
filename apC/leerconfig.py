import sys, manim

config = manim.config   # el mismo objeto de «from manim import *»

# Lectura como atributo (forma preferida) o como diccionario
print(config.pixel_width, config.pixel_height, config.frame_rate)
print(config["background_color"], config.quality)

# Propiedades derivadas: no están en ningún archivo, se calculan
print(round(config.frame_width, 4), config.frame_height,
      round(config.aspect_ratio, 4))
print(config.top, config.right_side)

# Coherencia interna: cambiar el radio vertical cambia la altura
config.frame_y_radius = 5.0
print(config.frame_height)

# tempconfig: un cambio que solo dura dentro del bloque «with»
with manim.tempconfig({"pixel_width": 1080, "pixel_height": 1920}):
    print("dentro:", config.pixel_width, config.pixel_height)
print("fuera:", config.pixel_width, config.pixel_height)
print(sys.version.split()[0], manim.__version__)
