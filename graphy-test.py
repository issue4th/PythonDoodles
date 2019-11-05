

# %%
import matplotlib.pyplot as plt
import numpy as np

def fn(listOfNumbers):
    result = []
    for number in listOfNumbers:
        result.append(number)
    return result

x = np.linspace(-2* np.pi, 2 * np.pi, 1000)

plt.plot(x, fn(x))

plt.show()

# %% [markdown]
# 
