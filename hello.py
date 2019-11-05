programmers='Ewan and Daddy'
print('Hello ' + programmers)
fruit = 'banana'
print(fruit)
parent='Mummy'
print(parent)
bug='red beetle'
print(bug)
zoo_animal='lion(he is lying)'
print(zoo_animal[0])
print(zoo_animal[1])
print(zoo_animal[2])
print(zoo_animal[3])
print(zoo_animal)

fruit_len = len(fruit)
print(fruit_len)
print('Length of ' + fruit + ' is ' + str(fruit_len))

print(programmers.lower())
print(programmers.upper())

print('-' * 10)
print(programmers * 3)
print(programmers + ' ' * 3)
print((programmers + ' ') * 3)

print('Hello {} '.format(programmers) * 3)

print('Length of {0} is {1}'.format(fruit, fruit_len))

fruit = input('Fruit:')
print('Length of {0} is {1}'.format(fruit, len(fruit)))

print(2 ** 3)