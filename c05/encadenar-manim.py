from manim import *

c = Circle(radius=1)
r = c.shift(UP).scale(2).set_color(RED)   # tres métodos seguidos
print("¿r es c?", r is c)                # cada método devolvió self
print("centro:", c.get_center(), "| ancho:", round(c.width, 3))

alias = c                                # otro nombre, mismo objeto
copia = c.copy()                          # un círculo nuevo, igual
alias.shift(RIGHT * 3)
print("c:", c.get_center(), "| copia:", copia.get_center())
