from numpy import random
import numpy as np

a1 = np.array([1, 2, 3, 4, 5])
random.shuffle(a1)
print(a1)

print('-----------------------------------')

a2 = np.array([1, 2, 3, 4, 5])
print(random.permutation(a2))

print('-----------------------------------')