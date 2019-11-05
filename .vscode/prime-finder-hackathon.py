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

highest_number_to_test = 100000

def generate_primes_up_to(number):
    primes = []
    primes.append(3)

    loops = 0
    for backbone in range(6, number, 6):
        
        possiblePrime = int(backbone - 1)
        if is_prime(possiblePrime, primes):
            primes.append(possiblePrime)
        
        possiblePrime = int(backbone + 1)
        if is_prime(possiblePrime, primes):
            primes.append(possiblePrime)

        loops += 1
        if loops % 100 == 0:
            print(backbone, len(primes) / backbone)

    primes.insert(0, 2)
    primes.insert(0, 1)

    return primes

def is_prime(possiblePrime, possibleDivisors):
    lastPossibleFactor = possiblePrime / 2 + 1

    for possibleDivisor in possibleDivisors:
        if possibleDivisor > lastPossibleFactor:
            break
        if possiblePrime % possibleDivisor == 0:
            return False

    return True 

def fn(index):
    return primes[int(index)]

def map(func, listOfNumbers):
    result = []
    for number in listOfNumbers:
        result.append(func(number))
    return result

def self_test():
    checkPrimes = generate_primes_up_to(50)
    if checkPrimes != [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
        print("Broken!")
        raise Exception("Self-test failed!")

self_test()
primes = generate_primes_up_to(highest_number_to_test)

x = np.linspace(0, len(primes)-1, len(primes))

plt.plot(x, map(fn, x))

plt.show()

