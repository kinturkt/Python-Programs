from numpy import random

x = random.normal(size=(2, 3))
print(x)

print('------------------------------------------')

y = random.normal(loc=1, scale=2, size=(2, 3))
print(y)

print('------------------------------------------')

z = random.normal(loc=1, scale=2, size=(2, 1))
print(z)