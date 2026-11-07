import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BarycentricInterpolator

# Target function (Runge function)
def f(x):
    return 1.0 / (1.0 + 25.0 * x**2)

n_values = [5, 10, 20]
x_eval = np.linspace(-1, 1, 1000)
f_true = f(x_eval)

print(f"{'n':<5} | {'Equally Spaced Max Error':<25} | {'Chebyshev Max Error':<25}")
print("-" * 60)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for idx, n in enumerate(n_values):
    # 1. Equally Spaced Nodes
    x_eq = np.linspace(-1, 1, n + 1)
    y_eq = f(x_eq)
    poly_eq = BarycentricInterpolator(x_eq, y_eq)
    pred_eq = poly_eq(x_eval)
    err_eq = np.max(np.abs(f_true - pred_eq))

    # 2. Chebyshev Nodes
    k = np.arange(n + 1)
    x_cheb = np.cos((2 * k + 1) * np.pi / (2 * (n + 1)))
    y_cheb = f(x_cheb)
    poly_cheb = BarycentricInterpolator(x_cheb, y_cheb)
    pred_cheb = poly_cheb(x_eval)
    err_cheb = np.max(np.abs(f_true - pred_cheb))

    # Print Table Row
    print(f"{n:<5} | {err_eq:<25.6e} | {err_cheb:<25.6e}")

    # Plot
    ax = axes[idx]
    ax.plot(x_eval, f_true, 'k--', label='True f(x)', linewidth=1.5)
    ax.plot(x_eval, pred_eq, 'r-', label='Equally Spaced')
    ax.plot(x_eval, pred_cheb, 'b-', label='Chebyshev')
    ax.set_title(f'Interpolation for n = {n}')
    ax.set_ylim(-0.2, 1.2)
    ax.legend()
    ax.grid(True)

plt.tight_layout()
plt.show()
