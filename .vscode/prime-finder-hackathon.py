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

highest_number_to_test = 1000000

def generate_primes_up_to(number):
    primes = [2, 3]

    possibleFactors = []
    lastPossiblePrimeFactorIndex = 1

    loops = 0
    for backbone in range(6, number, 6):
        
        possiblePrime = int(backbone - 1)
        lastPossiblePrimeFactor = np.sqrt(possiblePrime)
        while primes[lastPossiblePrimeFactorIndex] <= lastPossiblePrimeFactor:
            possibleFactors.append(primes[lastPossiblePrimeFactorIndex])
            lastPossiblePrimeFactorIndex += 1

        if is_prime_given_only_possible_factors(possiblePrime, possibleFactors):
            primes.append(possiblePrime)
        
        possiblePrime += 2
        lastPossiblePrimeFactor = np.sqrt(possiblePrime)
        while primes[lastPossiblePrimeFactorIndex] <= lastPossiblePrimeFactor:
            possibleFactors.append(primes[lastPossiblePrimeFactorIndex])
            lastPossiblePrimeFactorIndex += 1

        if is_prime_given_only_possible_factors(possiblePrime, possibleFactors):
            primes.append(possiblePrime)

        loops += 1
        if loops % 100 == 0:
            print(backbone, len(primes) / backbone)

    return primes

def is_prime_given_only_possible_factors(possiblePrime, possibleFactors):
    for possibleFactor in possibleFactors:
        if possiblePrime % possibleFactor == 0:
            return False

    return True 

def is_prime_given_all_primes(number, primes):
    possiblePrime = int(number)
    lastPossiblePrimeFactor = np.sqrt(possiblePrime)
    for possibleFactor in primes:
        if possibleFactor > lastPossiblePrimeFactor:
            return True
        if possiblePrime % possibleFactor == 0:
            return False

    return False 


def self_test():
    to100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    to200 = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    to300 = [211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]
    to400 = [307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397]
    to500 = [401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
    expectedPrimes = to100 + to200 + to300 + to400 + to500
    
    generatedPrimes = generate_primes_up_to(500)
    if generatedPrimes != expectedPrimes:
        print("Broken: ", generatedPrimes)
        index = 0
        while generatedPrimes[index] == expectedPrimes[index]:
            index += 1
        raise Exception("Self-test failed - mismatch at index ", index)

self_test()
primes = generate_primes_up_to(highest_number_to_test)

def plotPrimes(index):
    return primes[int(index)]

def plotOffsetToNextPrime(index):
    return primes[int(index) + 1] - primes[int(index)]

def plotPrimePositions(index):
    if is_prime_given_all_primes(int(index), primes):
        return index
    else:
        return 0

def map(func, listOfNumbers):
    result = []
    for number in listOfNumbers:
        result.append(func(number))
    return result

x = np.linspace(0, len(primes)-2, len(primes)-1)
x2 = np.linspace(0, highest_number_to_test, highest_number_to_test-1)

print("Generating graphs...")
plt.plot(x2, map(plotPrimePositions, x2))
plt.plot(x, map(plotPrimes, x))
plt.plot(x, map(plotOffsetToNextPrime, x))
#plt.bar(x, height=primePlot)

print("Displaying graphs...")
plt.show()

