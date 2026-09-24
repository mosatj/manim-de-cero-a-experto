from manim import *

grupo = VGroup(*[Dot() for _ in range(3)])
for retraso in [0, 0.5, 1]:
    anim = FadeIn(grupo, lag_ratio=retraso,
                  rate_func=linear)
    print(f"lag_ratio = {retraso}")
    for alpha in [0.25, 0.5, 0.75]:
        subs = [anim.get_sub_alpha(alpha, i, 3)
                for i in range(3)]
        texto = ", ".join(f"{s:.2f}" for s in subs)
        print(f"   alpha={alpha:.2f} -> [{texto}]")
