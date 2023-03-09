from numpy import random
x = random.randint(100)
print(x)
print('----------------------------------')

x1 = random.rand()
print(x1)
print('----------------------------------')

a = random.randint(50, size=(5))
print(a)
print('----------------------------------')

y = random.randint(100, size=(3, 5))
print(y)
print('----------------------------------')

y1 = random.rand(9)
print(y1)
print('----------------------------------')

x2 = random.choice([15, 35, 56, 78, 98, 10, 24, 18, 91, 101])
print(x2)
print('----------------------------------')

x3 = random.choice([3, 5, 7, 9], size=(3, 5))
print(x3)