import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2* np.pi, 2 * np.pi, 1000)

plt.plot(x, np.cos(x))
plt.plot(x, np.sin(x))
plt.plot(x, x * x)

plt.show()