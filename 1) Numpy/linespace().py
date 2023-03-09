import numpy as np

help(np.linspace)
print('---------------------------------------------')

# Examples

a = np.linspace(1,40, num=5)
print(a)

print('---------------------------------------------')

b = np.linspace(1,50, num=5, endpoint=False)
print(b)

print('---------------------------------------------')

c = np.linspace(1,10, dtype="int")
print(c)

print('---------------------------------------------')

d = np.linspace(1,30, num=5, retstep=True)
print(d)