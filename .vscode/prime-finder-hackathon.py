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

highest_number_to_test = 10000000

primes = []

def generate_primes_up_to(number):
    primes.append(1)
    primes.append(2)
    primes.append(3)

    loops = 0
    for backbone in range(6, number, 6):
        
        possiblePrime = int(backbone - 1)
        if is_prime(possiblePrime):
            primes.append(possiblePrime)
        
        possiblePrime = int(backbone + 1)
        if is_prime(possiblePrime):
            primes.append(possiblePrime)

        loops += 1
        if loops % 100 == 0:
            print(backbone, len(primes) / backbone)

def is_prime(possiblePrime):
    possibleDivisors = primes
    lastPossibleFactor = possiblePrime / 2 + 1

    for possibleDivisor in possibleDivisors:
        if possibleDivisor <= 1:
            continue
        if possibleDivisor > lastPossibleFactor:
            break
        if possiblePrime % possibleDivisor == 0:
            return False

    return True 

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

generate_primes_up_to(highest_number_to_test)
x = np.linspace(0, highest_number_to_test, highest_number_to_test)

#plt.plot(x, map(fn, x))
#plt.plot(x, map(fn2, x))

#plt.show()

