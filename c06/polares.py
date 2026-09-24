import numpy as np


def a_cartesianas(r, theta):
    return r * np.cos(theta), r * np.sin(theta)


def a_polares(x, y):
    return np.hypot(x, y), np.arctan2(y, x)  # atan2 ve el cuadrante


x, y = a_cartesianas(2, np.pi / 3)
print(f"(r, θ) = (2, π/3)  ->  (x, y) = ({x:.3f}, {y:.3f})")
r, th = a_polares(-1, -1)
print(f"(x, y) = (-1, -1)  ->  r = {r:.3f}, "
      f"θ = {np.degrees(th):.1f}°")

# Rosa de tres pétalos r = cos(3θ): la curva entera en dos líneas
theta = np.linspace(0, np.pi, 7)
r = np.cos(3 * theta)
xs, ys = a_cartesianas(r, theta)
print("θ (grados):", np.degrees(theta).round(0))
print("r         :", r.round(3) + 0.0)   # + 0.0 evita "-0."
print("x         :", xs.round(3) + 0.0)
