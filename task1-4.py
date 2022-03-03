import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_title("grafik")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid()
x = np.linspace(0, 5, 15)

k1 = 1
k2 = 5
plt.plot(x, k1 * x)
plt.plot(x, np.cos(k2 * x))

plt.show()
