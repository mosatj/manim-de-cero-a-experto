from manim import *


def cadena(clase):
    nombres = [c.__name__ for c in clase.mro()]
    return " > ".join(nombres[:-2])  # sin Animation, object


for clase in [Create, Uncreate, Write, FadeIn,
              ReplacementTransform, Rotate, Indicate,
              ScaleInPlace, Succession, LaggedStart, Wait]:
    print(f"{clase.__name__:>20}: {cadena(clase)}")
print()
for clase in [MovingCameraScene, ZoomedScene, ThreeDScene,
              LinearTransformationScene]:
    print(f"{clase.__name__:>25}:",
          " > ".join(c.__name__ for c in clase.mro()[1:-1]))
