import numpy as np

help(np.array)

print('Examples of array:')

# 0-D Array
a = np.array(25)
print(a)
print('---------------------------------------')


#1-D Array
a1 = np.array([1, 2, 3, 4, 5])
print(a1)
print(type(a1))
print('---------------------------------------')


# 2-D Array
a2 = np.array([[1, 2, 3], [4, 5, 6],])
print(a2)
print(a2.ndim)                     # To know the dimensions of the array
print('---------------------------------------')


b = np.ones((3,2))  # array of 1s
print(b)
print('---------------------------------------')

c = np.zeros((3,4)) # array of 0s
print(c)
print('----------------------------------------')

d = np.random.random(3) # array of random value
print(d)
print('----------------------------------------')

e = np.full((2,2),12) # array filled with constant values
print(e)
print('----------------------------------------')


# Creating a 5-D Array

f = np.array([1, 2, 3, 4], ndmin=5)

print(f)
print('Here, number of dimensions are :', f.ndim)