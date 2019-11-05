# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '..\\..\..\..\AppData\Local\Temp'))
	print(os.getcwd())
except:
	pass
# %%
import matplotlib.pyplot as plt
import numpy as np

primes = []

def is_prime(number):
    integer = abs(int(number))

    for possible in primes:
        if possible <= 1:
            continue
        if integer % int(possible) == 0:
            return 0
        if possible > integer / 2:
            break

    primes.append(integer)

    print(integer)
    return integer 

def fn(number):
    return np.sin(number)

def fn2(number):
    return is_prime(number)
#        return number
 #   else:
  #      return 0

def map(func, listOfNumbers):
    result = []
    for number in listOfNumbers:
        result.append(func(number))
    return result

x = np.linspace(0, 1000000, 1000001)

plt.plot(x, map(fn, x))
plt.plot(x, map(fn2, x))

plt.show()

