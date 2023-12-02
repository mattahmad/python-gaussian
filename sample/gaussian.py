import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, mu, sig):
    return (1.0 / (np.sqrt(2.0 * np.pi) * sig)) * np.exp(-np.power((x - mu) / sig, 2.0) / 2)

# Create an array of x values
x_values = np.linspace(-3, 3, 120)

# Plot Gaussian distributions for different (μ, σ) pairs
for mu, sig in [(-1, 1), (0, 2), (2, 3)]:
    plt.plot(x_values, gaussian(x_values, mu, sig), label=f"μ={mu}, σ={sig}")

plt.xlabel("x")
plt.ylabel("Probability Density")
plt.title("1-Dimensional Gaussian Distribution")
plt.legend()
plt.grid(True)
plt.show()