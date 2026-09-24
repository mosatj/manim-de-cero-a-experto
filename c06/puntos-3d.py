from manim import *

print("UP    =", UP, "  RIGHT =", RIGHT, "  OUT =", OUT)
print("UR    =", UR, "  (es UP + RIGHT)")
print("2*UP + 3*LEFT =", 2 * UP + 3 * LEFT)
print(type(UP).__name__, UP.dtype, UP.shape)
c = Circle().shift(2 * RIGHT + UP)
print("centro del círculo:", c.get_center())
print("borde superior    :", c.get_top())
