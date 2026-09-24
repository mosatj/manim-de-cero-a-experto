from manim import *


def paso_suave(t):                  # nuestra versión: 3t² − 2t³
    return 3 * t**2 - 2 * t**3


t = np.linspace(0, 1, 6)
print("t          :", t)
print("linear     :", np.round([linear(v) for v in t], 3))
print("paso_suave :", np.round(paso_suave(t), 3))
print("smoothstep :", np.round([smoothstep(v) for v in t], 3))
print("smooth     :", np.round([smooth(v) for v in t], 3))
print("there_and_back:",
      np.round([there_and_back(v) for v in t], 3))
