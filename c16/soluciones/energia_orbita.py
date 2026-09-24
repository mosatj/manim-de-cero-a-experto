from manim import *

GM, H = 40.0, 0.02


class EnergiaOrbita(Scene):
    def construct(self):
        v0 = 0.8 * np.sqrt(GM / 3)
        inicio = [np.array([3.0, 0]), np.array([0, v0])]
        estados = {"explícito": inicio, "semi": inicio}

        def energia(p, v):                   # cinética + potencial
            return 0.5 * v @ v - GM / np.linalg.norm(p)

        def paso(metodo):
            p, v = estados[metodo]
            a = -GM * p / np.linalg.norm(p) ** 3
            if metodo == "explícito":
                estados[metodo] = [p + H * v, v + H * a]
            else:
                v = v + H * a
                estados[metodo] = [p + H * v, v]

        reloj = ValueTracker(0)
        reloj.reserva = 0.0

        def avanzar(m, dt):                  # paso fijo
            m.reserva += dt
            while m.reserva >= H:
                paso("explícito")
                paso("semi")
                m.reserva -= H
                m.increment_value(H)

        reloj.add_updater(avanzar)
        filas = VGroup()
        for metodo, color in [("explícito", RED), ("semi", GREEN)]:
            numero = DecimalNumber(energia(*estados[metodo]),
                                   num_decimal_places=3,
                                   include_sign=True, color=color)
            numero.add_updater(lambda m, k=metodo: m.set_value(
                energia(*estados[k])))
            nombre = Text(metodo, color=color).scale(0.6)
            filas.add(VGroup(nombre, numero).arrange(buff=0.5))
        filas.arrange(DOWN, aligned_edge=LEFT)
        inicial = MathTex(rf"E_0 = {energia(*inicio):.3f}")
        tabla = VGroup(inicial, filas).arrange(DOWN, buff=0.6)
        self.add(reloj, tabla)
        self.wait(9)
