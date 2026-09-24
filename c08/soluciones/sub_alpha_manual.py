from manim import *

grupo = VGroup(*[Dot() for _ in range(5)])
anim = Create(grupo, lag_ratio=0.25, rate_func=linear)
# full_length = (5 - 1) * 0.25 + 1 = 2; value = 0.5 * 2 = 1
for i in range(5):
    sub = anim.get_sub_alpha(0.5, i, 5)
    print(f"submobject {i}: {sub:.2f}")
