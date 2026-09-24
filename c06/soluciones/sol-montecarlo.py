import numpy as np


def estimar_pi(n, semilla):
    p = np.random.default_rng(semilla).uniform(-1, 1, size=(n, 2))
    return 4 * np.mean((p**2).sum(axis=1) <= 1)


for n in (100, 10_000, 1_000_000):
    est = [estimar_pi(n, s) for s in range(5)]   # 5 semillas
    error = np.mean(np.abs(np.array(est) - np.pi))
    print(f"n = {n:>9,}: {np.round(est, 4)}  error {error:.4f}")
print("reproducible:", estimar_pi(500, 42) == estimar_pi(500, 42))
