import numpy as np

help(np.identity)
print('---------------------------------------------')

# Examples

x = np.identity(3, dtype="int")
print(x)

print('---------------------------------------------')

y = np.identity(2, dtype=float)
print(y)

print('---------------------------------------------')

help(np.eye)
print('---------------------------------------------')

# Examples     -> Syntax: np.eye(rows, columns)

a = np.eye(4)
print(a)

print('---------------------------------------------')

b = np.eye(4,5)
print(b)

print('---------------------------------------------')

c = np.eye(3, k=1)
print(c)

print('---------------------------------------------')

d = np.eye(5, k=1, dtype="int")
print(d)

print('---------------------------------------------')