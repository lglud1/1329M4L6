import matplotlib.pyplot as plt
import numpy as np

x_small = np.arange(1, 6)
y_small = x_small ** 3

plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.scatter(x_small, y_small, c=y_small, cmap='viridis')
plt.title('First 5 Cubic Numbers')
plt.xlabel('Number')
plt.ylabel('Cube')
plt.colorbar(label='Cube Value')

x_large = np.arange(1, 5001)
y_large = x_large ** 3

plt.subplot(2, 1, 2)
plt.scatter(x_large, y_large, c=y_large, cmap='viridis')
plt.title('First 5000 Cubic Numbers')
plt.xlabel('Number')
plt.ylabel('Cube')
plt.colorbar(label='Cube Value')

plt.tight_layout()
plt.savefig('cubes_plot.png')
plt.show()
