import numpy as np


def euler(f, t, y, h):
    return y + h * f(t, y)


def heun(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + h, y + h * k1)          # pendiente al final del paso
    return y + h / 2 * (k1 + k2)


def rk4(f, t, y, h):
    p1 = f(t, y)
    p2 = f(t + h / 2, y + h / 2 * p1)
    p3 = f(t + h / 2, y + h / 2 * p2)
    p4 = f(t + h, y + h * p3)
    return y + h / 6 * (p1 + 2 * p2 + 2 * p3 + p4)


def resolver(metodo, f, t0, y0, h, n):
    """Aplica n pasos del método; devuelve arrays t, y."""
    t, y = [t0], [y0]
    for _ in range(n):
        y.append(metodo(f, t[-1], y[-1], h))
        t.append(t[-1] + h)
    return np.array(t), np.array(y)


f = lambda t, y: y - t**2 + 1      # y' = y - t^2 + 1, y(0) = 0.5
exacta = lambda t: (t + 1)**2 - 0.5 * np.exp(t)

if __name__ == "__main__":        # solo al ejecutarlo directamente
    h, n = 0.2, 10
    t, ye = resolver(euler, f, 0.0, 0.5, h, n)
    _, yh = resolver(heun, f, 0.0, 0.5, h, n)
    _, yr = resolver(rk4, f, 0.0, 0.5, h, n)
    print(" t    exacta    Euler     Heun      RK4")
    for i in range(0, n + 1):
        print(f"{t[i]:.1f} {exacta(t[i]):9.6f} {ye[i]:9.6f}"
              f" {yh[i]:9.6f} {yr[i]:9.6f}")
    print("\nErrores absolutos |y(t_i) - y_i|")
    print(" t    Euler     Heun      RK4")
    for i in (1, 2, 3, 4, 5, 10):
        e = [abs(exacta(t[i]) - y[i]) for y in (ye, yh, yr)]
        print(f"{t[i]:.1f} {e[0]:.6f}  {e[1]:.6f}  {e[2]:.2e}")
