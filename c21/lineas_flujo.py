from manim import *


def pendulo(p):
    theta, omega = p[0], p[1]
    # Péndulo sin rozamiento: theta' = omega,  omega' = -sen(theta)
    return np.array([omega, -np.sin(theta), 0])


class LineasFlujo(Scene):
    def construct(self):
        lineas = StreamLines(
            pendulo, x_range=[-7, 7, 0.6], y_range=[-3.6, 3.6, 0.6],
            stroke_width=1.5, virtual_time=6, padding=0.5,
            max_anchors_per_line=40, colors=[BLUE, TEAL_D, GOLD_D])
        fijas = lineas.copy()        # copia intacta, sin animación
        self.add(lineas)
        lineas.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(4)
        # Detiene el flujo y muestra las líneas completas
        lineas.remove_updater(lineas.flow_animation)
        self.play(FadeOut(lineas), FadeIn(fijas))
        # Equilibrios: centro (0, 0) y puntos de silla (±pi, 0)
        centro = Dot(ORIGIN, color=WHITE)
        sillas = VGroup(Dot(PI * LEFT, color=RED),
                        Dot(PI * RIGHT, color=RED))
        self.play(FadeIn(centro, scale=3), FadeIn(sillas, scale=3))
