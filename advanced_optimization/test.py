import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from ipywidgets import interact, FloatLogSlider
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

def barrier_objective(z, t):
    x, y = z
    if 40 - 2*x - 2*y <= 0 or 14 - x <= 0 or x <= 0 or y <= 0:
        return np.inf
    area = x * y
    barrier = -(1/t) * (
        np.log(40 - 2*x - 2*y) +
        np.log(14 - x) +
        np.log(x) +
        np.log(y)
    )
    return -area + barrier

def plot_central_path(t):
    start_point = [5, 5]
    res = minimize(barrier_objective, start_point, args=(t,), method='BFGS')
    
    if not res.success:
        print("Optimization failed.")
        return
    
    x, y = res.x
    area = x * y

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 15)
    ax.grid(True)
    ax.set_title(f"Interior-Point Solution for t = {t:.2f}")
    ax.set_xlabel("x (Width)")
    ax.set_ylabel("y (Height)")

    x_vals = np.linspace(0.01, 14, 300)
    y1 = (40 - 2 * x_vals) / 2
    ax.plot(x_vals, y1, label="2x + 2y ≤ 40", color='green')
    ax.plot(x, y, 'ro', label=f"x={x:.2f}, y={y:.2f}, area={area:.2f}")
    ax.legend()
    plt.show()

interact(
    plot_central_path,
    t=FloatLogSlider(base=10, value=1, min=0, max=4, step=0.1, description='t')
)
