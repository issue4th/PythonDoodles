def getDigitsOf(number):
    return list(str(number))

def multiplyDigitsOf(number):
    digitsOfNumber = getDigitsOf(number)

    multipliedDigits = 1
    for digit in digitsOfNumber:
        nextDigit = int(digit)
        if (nextDigit > 0):
            multipliedDigits = multipliedDigits * nextDigit
        else:
            print("skipped a zero")
    
    return multipliedDigits

def reduceToOneDigit(number):
    numberOfReductions = 0
    multipliedDigits = multiplyDigitsOf(number)
    numberOfReductions += 1
    print("multipied digits:", multipliedDigits)
    
    while (multipliedDigits >= 10):
        multipliedDigits = multiplyDigitsOf(multipliedDigits)
        numberOfReductions = numberOfReductions + 1
        print("multipied digits:", multipliedDigits)
    
    print("number of reductions:",numberOfReductions)


number = input("Number:")
print(number)
reduceToOneDigit(number)

