from manim import *

print("Tipo:", type(config).__name__)
print("Píxeles:", config.pixel_width, "x",
      config.pixel_height, "a", config.frame_rate, "fps")
print("Marco:", round(config.frame_width, 4), "x",
      config.frame_height, "unidades")
print("Renderizador:", config.renderer.value)

with tempconfig({"quality": "low_quality"}):
    print("Dentro de tempconfig:", config.pixel_width, "x",
          config.pixel_height, "a", config.frame_rate, "fps")
print("Fuera otra vez:", config.pixel_width, "x",
      config.pixel_height)

config.frame_height = 10  # ¿cambia también el ancho?
print("frame_height=10 ->", "ancho:",
      round(config.frame_width, 4),
      "| y_radius:", config.frame_y_radius)
